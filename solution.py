import os
import json

from src.ocr.run_ocr import run_ocr
from src.extraction.extract_fields import extract_fields


class DocFusionSolution:

    def train(self, train_dir: str, work_dir: str) -> str:
        """
        Training step (not needed for rule-based pipeline)
        """

        model_dir = os.path.join(work_dir, "model")

        os.makedirs(model_dir, exist_ok=True)

        return model_dir


    def predict(self, model_dir: str, data_dir: str, out_path: str) -> None:

        images_dir = data_dir

        results = []

        for image in os.listdir(images_dir):

            image_path = os.path.join(images_dir, image)

            text = run_ocr(image_path)

            fields = extract_fields(text)

            record = {
                "id": image.replace(".jpg","").replace(".png",""),
                "vendor": fields["vendor"],
                "date": fields["date"],
                "total": fields["total"],
                "is_forged": 0
            }

            results.append(record)

        with open(out_path, "w") as f:
            for r in results:
                f.write(json.dumps(r) + "\n")