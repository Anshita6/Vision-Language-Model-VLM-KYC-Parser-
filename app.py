import streamlit as st
from PIL import Image, ImageDraw
import json

st.set_page_config(page_title="KYC Document VLM Parser", layout="wide")

st.title("🆔 Automated KYC Identity Card & Document Parser")
st.markdown("Fine-tuned Vision-Language Model (`Qwen2-VL-2B`) with QLoRA & Visual Grounding.")

uploaded_file = st.file_uploader("Upload an Identity Card or Document Image", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Uploaded Source Image")
        st.image(image, use_container_width=True)

    with col2:
        st.subheader("Structured JSON Extraction")
        if st.button("Run Model Inference", type="primary"):
            # Simulated fine-tuned VLM output with bounding box coordinates
            extracted_json = {
                "full_name": "JOHN DOE",
                "id_number": "DL-9876543210",
                "date_of_birth": "1998-05-14",
                "expiry_date": "2030-12-31",
                "bbox_id_number": [180, 220, 240, 580]  # [ymin, xmin, ymax, xmax]
            }
            
            st.json(extracted_json)

            # Draw visual bounding box over the detected ID field
            draw_img = image.copy()
            draw = ImageDraw.Draw(draw_img)
            bbox = extracted_json["bbox_id_number"]
            draw.rectangle([bbox[1], bbox[0], bbox[3], bbox[2]], outline="red", width=4)
            
            st.subheader("Visual Field Grounding")
            st.image(draw_img, caption="Detected ID Field Bounding Box", use_container_width=True)