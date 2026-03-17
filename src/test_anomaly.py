from ocr.run_ocr import run_ocr
from anomaly.detect_anomaly import detect_forgery, load_gt_text

image = "../data/raw/findit2/train/X00016469622.png"
txt = "../data/raw/findit2/train/X00016469622.txt"

ocr_text = run_ocr(image)
gt_text = load_gt_text(txt)

result = detect_forgery(ocr_text, gt_text)

print("Forgery Prediction:", result)