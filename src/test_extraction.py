from ocr.run_ocr import run_ocr
from extraction.extract_fields import extract_fields


image_path = "../data/raw/sroie2019/train/img/X00016469612.jpg"

text = run_ocr(image_path)

result = extract_fields(text)

print(result)