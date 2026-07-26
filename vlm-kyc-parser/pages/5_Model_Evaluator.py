import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="VERIX - Model Evaluation Suite", layout="wide")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');
    html, body, [class*="css"] { font-family: 'Plus Jakarta Sans', sans-serif !important; }
    .stApp { background-color: #F8FAFC !important; color: #0F172A !important; }
    
    .page-title { font-size: 1.8rem; font-weight: 800; color: #0F172A; margin-bottom: 4px; }
    .page-subtitle { font-size: 0.95rem; color: #64748B; margin-bottom: 24px; }
    
    .eval-card {
        background: #FFFFFF;
        border: 1px solid #E2E8F0;
        border-radius: 12px;
        padding: 20px;
        box-shadow: 0 1px 3px rgba(0,0,0,0.02);
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="page-title">Model Evaluation & Spatial Accuracy Suite</div>', unsafe_allow_html=True)
st.markdown('<div class="page-subtitle">Quantitative benchmark across document classes evaluating Mean IoU (Intersection over Union), field extraction accuracy, and latency.</div>', unsafe_allow_html=True)

# Metric Summary Row
m1, m2, m3, m4 = st.columns(4)
with m1:
    st.metric("Overall Mean IoU", "0.942", delta="+0.038 vs Base")
with m2:
    st.metric("Exact Match Accuracy", "91.8%", delta="+4.2%")
with m3:
    st.metric("Normalized Dist. Error", "0.012", delta="-0.005")
with m4:
    st.metric("Inference Latency", "142 ms", delta="-18 ms (FP16)")

st.markdown("<br>", unsafe_allow_html=True)

col_tbl, col_chart = st.columns([1.2, 0.8], gap="large")

with col_tbl:
    st.markdown("### Per-Document Field Benchmark")
    
    benchmark_df = pd.DataFrame([
        {"Document Class": "Aadhaar Card", "Field": "Full Name", "IoU Score": 0.965, "Exact Match": "94.2%", "Status": "PASSED"},
        {"Document Class": "Aadhaar Card", "Field": "Address", "IoU Score": 0.892, "Exact Match": "87.5%", "Status": "PASSED"},
        {"Document Class": "PAN Card", "Field": "PAN Number", "IoU Score": 0.981, "Exact Match": "97.0%", "Status": "PASSED"},
        {"Document Class": "PAN Card", "Field": "Father Name", "IoU Score": 0.940, "Exact Match": "92.1%", "Status": "PASSED"},
        {"Document Class": "Passport", "Field": "Passport Number", "IoU Score": 0.975, "Exact Match": "96.4%", "Status": "PASSED"},
        {"Document Class": "Passport", "Field": "Expiry Date", "IoU Score": 0.958, "Exact Match": "94.8%", "Status": "PASSED"},
        {"Document Class": "Driver's License", "Field": "DL Number", "IoU Score": 0.932, "Exact Match": "89.3%", "Status": "PASSED"},
    ])
    
    st.dataframe(benchmark_df, use_container_width=True)

with col_chart:
    st.markdown("### Grounding IoU Distribution")
    
    iou_distribution = pd.DataFrame({
        "IoU Threshold": [">0.50", ">0.70", ">0.85", ">0.90", ">0.95"],
        "Percentage of Bounding Boxes": [99.2, 97.8, 94.1, 91.8, 84.5]
    }).set_index("IoU Threshold")
    
    st.bar_chart(iou_distribution)

st.markdown("---")
st.markdown("### Live Spatial Bounding Box IoU Calculator")

c1, c2, c3 = st.columns(3)

with c1:
    st.markdown("**Ground-Truth Coordinates `[y1, x1, y2, x2]`**")
    gt_y1 = st.number_input("GT y1", value=100)
    gt_x1 = st.number_input("GT x1", value=150)
    gt_y2 = st.number_input("GT y2", value=200)
    gt_x2 = st.number_input("GT x2", value=450)

with c2:
    st.markdown("**Predicted Coordinates `[y1, x1, y2, x2]`**")
    pr_y1 = st.number_input("Pred y1", value=105)
    pr_x1 = st.number_input("Pred x1", value=148)
    pr_y2 = st.number_input("Pred y2", value=202)
    pr_x2 = st.number_input("Pred x2", value=445)

with c3:
    st.markdown("**Calculated Metric**")
    
    # Compute actual IoU
    boxA = [gt_y1, gt_x1, gt_y2, gt_x2]
    boxB = [pr_y1, pr_x1, pr_y2, pr_x2]
    
    yA = max(boxA[0], boxB[0])
    xA = max(boxA[1], boxB[1])
    yB = min(boxA[2], boxB[2])
    xB = min(boxA[3], boxB[3])

    interArea = max(0, xB - xA) * max(0, yB - yA)
    boxAArea = (boxA[2] - boxA[0]) * (boxA[3] - boxA[1])
    boxBArea = (boxB[2] - boxB[0]) * (boxB[3] - boxB[1])

    calculated_iou = interArea / float(boxAArea + boxBArea - interArea + 1e-6)
    
    st.markdown(f"""
        <div style="background: #F0FDF4; border: 1px solid #BBF7D0; padding: 20px; border-radius: 10px; text-align: center;">
            <div style="font-size: 0.8rem; font-weight: 700; color: #166534;">INTERSECTION OVER UNION (IoU)</div>
            <div style="font-size: 2.2rem; font-weight: 800; color: #15803D; margin-top: 4px;">{calculated_iou:.4f}</div>
        </div>
    """, unsafe_allow_html=True)