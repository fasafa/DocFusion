# DocFusion AI – Intelligent Document Processing Pipeline

## Overview

DocFusion AI is an end-to-end machine learning pipeline designed to process unstructured document images such as receipts and invoices. The system extracts structured information and detects anomalies, enabling efficient and automated document understanding in real-world scenarios.

---

## Problem Statement

Organizations process thousands of documents daily, but most data is locked inside:

* Scanned PDFs
* Receipt images
* Unstructured formats

Manual processing is slow, error-prone, and inefficient.
This project automates document understanding, data extraction, and anomaly detection.

---

## Solution Pipeline

```
Image
 ↓
OCR (EasyOCR)
 ↓
Text Extraction
 ↓
Field Extraction (Vendor, Date, Total)
 ↓
Anomaly Detection
 ↓
Structured Output (JSONL)
```

---

##  Key Features

* 📄 OCR using EasyOCR
* 🔍 Extraction of key fields:

  * Vendor
  * Date
  * Total Amount
* 🚨 Rule-based anomaly detection
* ⚡ Batch document processing pipeline
* 📦 Autograder-ready (`solution.py`)
* 🌐 Streamlit Web UI for interactive usage

---

## 🗂 Project Structure

```
docfusion/
│
├── src/
│   ├── ocr/
│   │   └── run_ocr.py
│   │
│   ├── extraction/
│   │   └── extract_fields.py
│   │
│   ├── anomaly/
│   │   └── detect_anomaly.py
│   │
│   └── pipeline/
│       └── run_pipeline.py
│
├── ui/
│   └── app.py
│
├── notebooks/
│   ├── 01_eda.ipynb
│   └── 02_information_extraction.ipynb
│
├── solution.py
├── requirements.txt
├── README.md
└── test_solution.py
```

---

##  Datasets Used

* **SROIE Dataset** – Receipt OCR and structured extraction
* **CORD Dataset** – Diverse layouts and variations
* **Find-It-Again Dataset** – Forgery and anomaly detection

---

##  Installation

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Pipeline

```bash
python src/pipeline/run_pipeline.py
```

Output will be generated at:

```
data/processed/predictions.jsonl
```

---

##  Run Autograder Simulation

```bash
python test_solution.py
```

This simulates the evaluation process using `solution.py`.

---

## Run Web Application

```bash
streamlit run ui/app.py
```

Features:

* Upload receipt image
* View extracted data
* Detect suspicious documents
* Inspect raw OCR text

---

##  Output Format

The system generates structured output in JSONL format:

```json
{"id":"X0001","vendor":"ABC Store","date":"2024-01-01","total":"10.00","is_forged":0}
```

---

## 🚨 Anomaly Detection Logic

The system uses a rule-based approach:

* Missing key fields → Suspicious
* OCR inconsistencies → Suspicious
* Valid structured output → Genuine

This can be extended to ML-based models.

---

##  Limitations

* OCR noise may affect extraction accuracy
* Some fields may be missing due to poor image quality
* Rule-based anomaly detection is basic and can be improved

---

##  Future Improvements

* Deep learning models (LayoutLM, Donut)
* Advanced anomaly detection using ML
* Bounding box visualization on documents
* Cloud deployment and API integration

---



---

## 📌 Final Note

This project demonstrates a **production-ready document processing system**, combining OCR, structured data extraction, anomaly detection, and a user-friendly interface.

It is designed with scalability, modularity, and real-world applicability in mind.
