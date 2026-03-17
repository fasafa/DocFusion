import difflib


def load_gt_text(txt_path):

    with open(txt_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    return [line.strip() for line in lines]


def detect_forgery(ocr_text, gt_text):

    ocr_join = " ".join(ocr_text)
    gt_join = " ".join(gt_text)

    similarity = difflib.SequenceMatcher(
        None, ocr_join, gt_join
    ).ratio()

    # rule
    if similarity < 0.6:
        return 1
    else:
        return 0