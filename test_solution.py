from solution import DocFusionSolution

solution = DocFusionSolution()

model_dir = solution.train("data/raw/SROIE2019/train/img", "models")

solution.predict(
    model_dir=model_dir,
    data_dir="data/raw/SROIE2019/train/img",
    out_path="predictions2.jsonl"
)

print("Test finished")