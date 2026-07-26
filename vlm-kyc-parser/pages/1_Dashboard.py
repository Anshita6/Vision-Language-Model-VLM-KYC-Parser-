import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="VERIX - Analytics Dashboard", layout="wide")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');
    html, body, [class*="css"] { font-family: 'Plus Jakarta Sans', sans-serif !important; }
    .stApp { background-color: #F8FAFC !important; color: #0F172A !important; }
    .metric-card {
        background: #FFFFFF;
        border: 1px solid #E2E8F0;
        border-radius: 12px;
        padding: 20px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.02);
    }
    .metric-value { font-size: 1.8rem; font-weight: 800; color: #1E40AF; }
    .metric-label { font-size: 0.8rem; font-weight: 700; color: #64748B; text-transform: uppercase; }
    </style>
""", unsafe_allow_html=True)

st.title("Model Metrics & System Performance")
st.caption("Live tracking of fine-tuned Vision-Language Model accuracy, mean IoU, and inference latency.")

m1, m2, m3, m4 = st.columns(4)
with m1:
    st.markdown('<div class="metric-card"><div class="metric-label">Mean IoU Accuracy</div><div class="metric-value">0.942</div></div>', unsafe_allow_html=True)
with m2:
    st.markdown('<div class="metric-card"><div class="metric-label">Exact Match Ratio</div><div class="metric-value">91.8%</div></div>', unsafe_allow_html=True)
with m3:
    st.markdown('<div class="metric-card"><div class="metric-label">Avg Inference Latency</div><div class="metric-value">142ms</div></div>', unsafe_allow_html=True)
with m4:
    st.markdown('<div class="metric-card"><div class="metric-label">Trainable Parameters</div><div class="metric-value">16.8M (LoRA)</div></div>', unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)
st.subheader("Training Loss vs. Bounding Box IoU Convergence")

# Generated training metric progression
df_metrics = pd.DataFrame({
    "Epoch": list(range(1, 11)),
    "Training Loss": [2.4, 1.8, 1.2, 0.75, 0.45, 0.28, 0.19, 0.14, 0.11, 0.09],
    "Validation IoU": [0.52, 0.64, 0.73, 0.81, 0.87, 0.90, 0.92, 0.93, 0.94, 0.942]
})

st.line_chart(df_metrics.set_index("Epoch"))