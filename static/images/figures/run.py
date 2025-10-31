import os
from pdf2image import convert_from_path
from PIL import Image, ImageChops
def trim(img: Image.Image):
    bg = Image.new(img.mode, img.size, img.getpixel((0,0)))
    diff = ImageChops.difference(img, bg)
    diff = ImageChops.add(diff, diff, 2.0, -5)
    bbox = diff.getbbox()
    if bbox:
        return img.crop(bbox)
    return img

# 要处理的文件夹路径
pdf_folder = r"/Users/ziyuguo/Downloads/Video_CoF/figures"
output_folder = r"/Users/ziyuguo/Desktop/Desktop-MacBookPro/Research/Video-Reasoning/sciverse-cuhk.github.io-main/static/images/figures"

os.makedirs(output_folder, exist_ok=True)

for filename in os.listdir(pdf_folder):
    if filename.lower().endswith(".pdf"):
        pdf_path = os.path.join(pdf_folder, filename)
        
        # 读取 PDF
        pages = convert_from_path(pdf_path)

        # 为每个 PDF 建立独立子目录
        base_name = os.path.splitext(filename)[0]
        pdf_output_dir = os.path.join(output_folder, base_name)
        # os.makedirs(pdf_output_dir, exist_ok=True)

        # 保存每一页
        for idx, page in enumerate(pages):
            page = trim(page)  # ✨ 去白边
            png_path = f"/Users/ziyuguo/Desktop/Desktop-MacBookPro/Research/Video-Reasoning/sciverse-cuhk.github.io-main/static/images/figures/{base_name}.png"
            page.save(png_path, "PNG")
        
        print(f"✅ 转换完成: {filename}")

print("🎉 所有 PDF 转换完成!")

