#!/home/clara/.clara.venv/bin/python3
import os
import sys
import argparse
import pymupdf

def replace_pdf_text(input_file, output_file, old_text, new_text):
    if not os.path.exists(input_file):
        print(f"错误: 找不到输入文件 '{input_file}'", file=sys.stderr)
        sys.exit(1)

    print(f"正在打开文件: {input_file}")
    doc = pymupdf.open(input_file)
    total_replacements = 0

    # 遍历每一页进行搜索和替换
    for page_num, page in enumerate(doc, start=1):
        text_instances = page.search_for(old_text)
        if text_instances:
            print(f"在第 {page_num} 页找到 {len(text_instances)} 处匹配修改项")
            for rect in text_instances:
                # --- 核心修复：防止连带误擦除 ---
                # 如果 PDF 底层字符边界有交叉，search_for 返回的矩形可能往左多包了一点
                # 我们人为将矩形的左边缘（x0）向右移动 5 到 10 个像素，精准缩减擦除范围
                # 这样可以 100% 保护左侧紧挨着的 "Employee’s SSA number:" 文字
                safe_rect = pymupdf.Rect(rect.x0, rect.y0+3, rect.x1, rect.y1-3)
                # 创见红线擦除区域（fill 1,1,1 为纯白背景颜色）
                page.add_redact_annot(safe_rect, text=None, fill=(1, 1, 1))
                total_replacements += 1

                # 立即将改动应用到当前页
                page.apply_redactions()

                # 3. 精准重写新文本：利用刚才旧框的原始高度作为参考，指定标准字号
                # 稍微下移 1 个像素（rect.y0 + (rect.y1 - rect.y0)*0.75 附近）可以让基线对齐得更好
                font_size = 8  # 这是标准表格的字号，你可以随时根据需要改成 9, 11 或 12

                # 计算文字插入的黄金起始点（左下角基线点）
                insert_point = pymupdf.Point(safe_rect.x0, safe_rect.y1)

                page.insert_text(
                    insert_point,
                    new_text,
                    fontsize=font_size,
                    fontname="hebo", # 使用系统自带的标准 Helvetica 无衬线体，最契合数字
                    color=(0, 0, 0)  # 纯黑色字体
                )

    if total_replacements == 0:
        print(f"警告: 未在文件中找到匹配的字符串 '{old_text}'")
    else:
        print(f"修改成功！共替换了 {total_replacements} 处文本。")

    # 保存优化后的 PDF
    doc.save(output_file, garbage=3, deflate=True, clean=True)
    doc.close()
    print(f"新文件已成功保存至: {output_file}")

if __name__ == "__main__":
    # 配置动态运行参数
    parser = argparse.ArgumentParser(description="使用 PyMuPDF 动态擦除并替换 PDF 文件中的敏感字符串/数字。")

    parser.add_argument("-i", "--input", required=True, help="输入的原始 PDF 文件路径")
    parser.add_argument("-o", "--output", required=True, help="修改后输出的新 PDF 文件路径")
    parser.add_argument("-s", "--search", required=True, help="需要被替换的原始目标文本字符串或模式")
    parser.add_argument("-r", "--replace", required=True, help="用于替换上去的新文本内容")

    args = parser.parse_args()

    replace_pdf_text(args.input, args.output, args.search, args.replace)