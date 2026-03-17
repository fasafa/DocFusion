import sys
import os

# Fix import path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
from PIL import Image
import tempfile

from src.ocr.run_ocr import run_ocr
from src.extraction.extract_fields import extract_fields
from src.anomaly.detect_anomaly import detect_forgery, load_gt_text


# Page config
st.set_page_config(
    page_title="DocFusion AI",
    page_icon="📄",
    layout="centered"
)

st.markdown(
    """
    <h1 style='text-align: center;'>📄 DocFusion AI</h1>
    <h4 style='text-align: center; color: gray;'>
    Intelligent Document Processing & Fraud Detection
    </h4>
    """,
    unsafe_allow_html=True
)

st.divider()

uploaded_file = st.file_uploader("📤 Upload a Receipt", type=["jpg", "png"])

if uploaded_file is not None:

    # Show image
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Receipt", use_column_width=True)

    # Save temp file
    with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as tmp:
        image.save(tmp.name)
        temp_path = tmp.name

    with st.spinner("🔍 Processing document..."):

        # OCR
        text = run_ocr(temp_path)

        # Extraction
        fields = extract_fields(text)

        # --------- Anomaly Detection ---------
        is_forged = 0

        # Rule-based improvement
        if fields["total"] is None:
            is_forged = 1
        elif fields["vendor"] is None:
            is_forged = 1

    st.divider()

    # --------- Display Results ---------
    st.subheader("📊 Extracted Information")

    col1, col2, col3 = st.columns(3)

    col1.metric("🏪 Vendor", fields["vendor"] if fields["vendor"] else "N/A")
    col2.metric("📅 Date", fields["date"] if fields["date"] else "N/A")
    col3.metric("💰 Total", fields["total"] if fields["total"] else "N/A")

    st.divider()

    # --------- Fraud Result ---------
    st.subheader("🚨 Fraud Detection")

    if is_forged == 1:
        st.error("⚠️ Suspicious / Possibly Forged Document")
    else:
        st.success("✅ Genuine Document")

    st.divider()

    # --------- Raw OCR Toggle ---------
    with st.expander("📝 View Raw OCR Text"):
        st.write(text)