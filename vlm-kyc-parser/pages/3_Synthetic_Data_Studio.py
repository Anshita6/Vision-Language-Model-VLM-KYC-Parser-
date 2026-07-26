import streamlit as st
import json
import random
import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageEnhance

st.set_page_config(page_title="VERIX - Synthetic Data Studio", layout="wide")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');
    html, body, [class*="css"] { font-family: 'Plus Jakarta Sans', sans-serif !important; }
    .stApp { background-color: #F8FAFC !important; color: #0F172A !important; }
    
    .page-title { font-size: 1.8rem; font-weight: 800; color: #0F172A; margin-bottom: 4px; }
    .page-subtitle { font-size: 0.95rem; color: #64748B; margin-bottom: 24px; }
    
    .info-card {
        background: #FFFFFF;
        border: 1px solid #E2E8F0;
        border-radius: 12px;
        padding: 20px;
        margin-bottom: 20px;
        box-shadow: 0 1px 3px rgba(0,0,0,0.02);
    }
    .metric-badge {
        background: #EFF6FF;
        color: #1E40AF;
        padding: 4px 10px;
        border-radius: 6px;
        font-size: 0.8rem;
        font-weight: 700;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="page-title">Synthetic Data Generation Engine</div>', unsafe_allow_html=True)
st.markdown('<div class="page-subtitle">Generate synthetic training samples with controlled augmentations (blur, rotation, perspective shift, shadow) and normalized bounding-box annotations.</div>', unsafe_allow_html=True)

col_ctrl, col_prev = st.columns([0.85, 1.15], gap="large")

with col_ctrl:
    st.markdown('<div class="info-card">', unsafe_allow_html=True)
    st.markdown("### Augmentation Parameters")
    
    doc_class = st.selectbox("Target Class", ["Aadhaar Card", "PAN Card", "Passport", "Driver's License"])
    num_samples = st.slider("Batch Sample Count", min_value=5, max_value=100, value=25)
    
    st.markdown("---")
    st.markdown("#### Noise Injection Controls")
    gaussian_blur = st.slider("Gaussian Blur Radius", 0.0, 3.0, 0.8, 0.1)
    brightness_var = st.slider("Brightness Shift", 0.5, 1.5, 1.0, 0.05)
    rotation_angle = st.slider("Max Rotation Angle (°)", 0, 15, 3)
    add_shadow = st.checkbox("Simulate Shadow / Lighting Gradient", value=True)
    add_perspective = st.checkbox("Simulate Perspective Tilt (3D Distortion)", value=False)
    
    generate_btn = st.button("Generate Synthetic Dataset Batch")
    st.markdown('</div>', unsafe_allow_html=True)

with col_prev:
    st.markdown("### Preview & Data Verification")
    
    # Generate mock synthetic document image with annotations
    def generate_synthetic_image():
        img = Image.new("RGB", (600, 380), color=(245, 247, 250))
        draw = ImageDraw.Draw(img)
        
        # Draw header banner
        draw.rectangle([20, 20, 580, 70], fill=(30, 64, 175))
        draw.text((35, 35), f"GOVERNMENT OF INDIA - {doc_class.upper()}", fill=(255, 255, 255))
        
        # Simulated photo box
        draw.rectangle([40, 100, 160, 260], fill=(210, 215, 225), outline=(150, 150, 150), width=2)
        draw.text((65, 170), "PHOTO", fill=(100, 100, 100))
        
        # Field text
        fields = {
            "name": {"val": "SYNTHETIC SAMPLE", "bbox": [100, 190, 130, 500]},
            "dob": {"val": "01/01/1998", "bbox": [140, 190, 165, 380]},
            "id_num": {"val": "XXXX-XXXX-9999", "bbox": [280, 120, 320, 480]}
        }
        
        for k, v in fields.items():
            draw.text((v["bbox"][1], v["bbox"][0]), f"{k.upper()}: {v['val']}", fill=(15, 23, 42))
            
        # Apply augmentations
        if gaussian_blur > 0:
            img = img.filter(ImageFilter.GaussianBlur(gaussian_blur))
        
        enhancer = ImageEnhance.Brightness(img)
        img = enhancer.enhance(brightness_var)
        
        if rotation_angle > 0:
            angle = random.uniform(-rotation_angle, rotation_angle)
            img = img.rotate(angle, expand=False, fillcolor=(245, 247, 250))
            
        return img, fields

    synth_img, synth_fields = generate_synthetic_image()
    
    st.image(synth_img, caption="Generated Synthetic Artifact (Augmented)", use_container_width=True)
    
    st.markdown("#### Grounding Annotation (JSON Lines Output)")
    
    sample_annotation = {
        "id": "synth_doc_00921",
        "doc_type": doc_class,
        "width": 600,
        "height": 380,
        "augmentations": {
            "blur_radius": gaussian_blur,
            "brightness": brightness_var,
            "rotation_deg": rotation_angle
        },
        "grounded_fields": {
            "full_name": {"text": "SYNTHETIC SAMPLE", "bbox_normalized": [263, 316, 342, 833]},
            "document_id": {"text": "XXXX-XXXX-9999", "bbox_normalized": [736, 200, 842, 800]}
        }
    }
    
    st.code(json.dumps(sample_annotation, indent=2), language="json")