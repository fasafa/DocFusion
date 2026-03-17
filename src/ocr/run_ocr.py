# import easyocr
# import cv2
# import os

# reader = easyocr.Reader(['en'])

# def run_ocr(image_path):
#     image = cv2.imread(image_path)

#     results = reader.readtext(image)

#     extracted_text = []

#     for bbox, text, confidence in results:
#         extracted_text.append(text)

#     return extracted_text


# if __name__ == "__main__":

#     sample = "../../data/raw/SROIE2019/train/img/X00016469612.jpg"

#     text = run_ocr(sample)

#     print(text)
import easyocr
import cv2

# load OCR model ONCE
reader = easyocr.Reader(['en'], gpu=False)

def run_ocr(image_path):

    image = cv2.imread(image_path)

    results = reader.readtext(image)

    extracted_text = []

    for bbox, text, confidence in results:
        extracted_text.append(text)

    return extracted_text    