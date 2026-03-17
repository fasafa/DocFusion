import os
import json
from tqdm import tqdm
import sys

# Allow importing modules from src
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from ocr.run_ocr import run_ocr
from extraction.extract_fields import extract_fields
from anomaly.detect_anomaly import detect_forgery, load_gt_text


# Paths
IMAGE_FOLDER = "data/raw/sroie2019/train/img"
FINDIT_FOLDER = "data/raw/findit2/train"
OUTPUT_FILE = "data/processed/predictions.jsonl"


def process_documents():

    results = []

    images = os.listdir(IMAGE_FOLDER)[:10]   # limit to 10 for testing

    for image in tqdm(images):

        image_path = os.path.join(IMAGE_FOLDER, image)

        # Run OCR
        text = run_ocr(image_path)

        # Extract fields
        fields = extract_fields(text)

        # ---------- Anomaly Detection ----------
        txt_name = image.replace(".jpg", ".txt")
        txt_path = os.path.join(FINDIT_FOLDER, txt_name)

        if os.path.exists(txt_path):
            gt_text = load_gt_text(txt_path)
            is_forged = detect_forgery(text, gt_text)
        else:
            is_forged = 0

        # ---------- Record ----------
        record = {
            "id": image.replace(".jpg", ""),
            "vendor": fields["vendor"],
            "date": fields["date"],
            "total": fields["total"],
            "is_forged": is_forged
        }

        results.append(record)

    return results


def save_jsonl(results, output_path):

    with open(output_path, "w") as f:
        for row in results:
            f.write(json.dumps(row) + "\n")


if __name__ == "__main__":

    results = process_documents()

    save_jsonl(results, OUTPUT_FILE)

    print("Pipeline finished. Predictions saved")