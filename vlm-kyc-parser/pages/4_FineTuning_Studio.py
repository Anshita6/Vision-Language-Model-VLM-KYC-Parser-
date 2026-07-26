import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="VERIX - PEFT/LoRA Training Studio", layout="wide")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');
    html, body, [class*="css"] { font-family: 'Plus Jakarta Sans', sans-serif !important; }
    .stApp { background-color: #F8FAFC !important; color: #0F172A !important; }
    
    .page-title { font-size: 1.8rem; font-weight: 800; color: #0F172A; margin-bottom: 4px; }
    .page-subtitle { font-size: 0.95rem; color: #64748B; margin-bottom: 24px; }
    
    .config-card {
        background: #FFFFFF;
        border: 1px solid #E2E8F0;
        border-radius: 12px;
        padding: 20px;
        box-shadow: 0 1px 3px rgba(0,0,0,0.02);
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="page-title">PEFT / LoRA Fine-Tuning Sandbox</div>', unsafe_allow_html=True)
st.markdown('<div class="page-subtitle">Configure Parameter-Efficient Fine-Tuning hyper-parameters on open-weight Vision-Language backbones (PaliGemma / LLaVA).</div>', unsafe_allow_html=True)

col_cfg, col_train = st.columns([1, 1], gap="large")

with col_cfg:
    st.markdown('<div class="config-card">', unsafe_allow_html=True)
    st.markdown("### Model & LoRA Hyperparameters")
    
    base_architecture = st.selectbox(
        "Base VLM Backbone",
        ["google/paligemma-3b-pt-224", "llava-hf/llava-1.5-7b-hf", "Qwen/Qwen2-VL-2B-Instruct"]
    )
    
    st.markdown("#### PEFT / LoRA Configuration")
    lora_r = st.select_slider("LoRA Rank (r)", options=[4, 8, 16, 32, 64], value=16)
    lora_alpha = st.select_slider("LoRA Alpha (α)", options=[8, 16, 32, 64, 128], value=32)
    lora_dropout = st.slider("LoRA Dropout", 0.0, 0.2, 0.05, 0.01)
    
    st.markdown("#### Target Linear Projection Modules")
    c1, c2 = st.columns(2)
    with c1:
        st.checkbox("q_proj", value=True)
        st.checkbox("v_proj", value=True)
        st.checkbox("k_proj", value=True)
    with c2:
        st.checkbox("out_proj", value=True)
        st.checkbox("fc1 / fc2", value=False)
        st.checkbox("vision_tower.proj", value=True)
        
    st.markdown("#### Optimization & Precision")
    quantization = st.radio("Quantization Precision", ["4-bit NF4 (QLoRA)", "8-bit Int8", "FP16 Mixed Precision", "BF16 Pure"], index=0)
    learning_rate = st.select_slider("Learning Rate", options=[1e-5, 5e-5, 1e-4, 2e-4, 5e-4], value=2e-4)
    batch_size = st.selectbox("Per-GPU Batch Size", [1, 2, 4, 8, 16], index=2)
    
    st.button("Launch Fine-Tuning Job")
    st.markdown('</div>', unsafe_allow_html=True)

with col_train:
    st.markdown("### Real-Time Training Metrics")
    
    st.markdown("**Trainable Parameter Analysis:**")
    st.json({
        "total_params": "3,110,542,848",
        "trainable_params": "16,777,216",
        "trainable_percentage": "0.5393%",
        "estimated_vram_gb": "6.8 GB (Fits on single RTX 3090/4090)"
    })
    
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("**Loss Convergence (Simulated Training Run):**")
    
    epochs = np.arange(1, 21)
    train_loss = 2.5 * np.exp(-0.25 * epochs) + np.random.normal(0, 0.02, 20)
    val_loss = 2.6 * np.exp(-0.22 * epochs) + np.random.normal(0, 0.03, 20)
    
    chart_data = pd.DataFrame({
        "Epoch": epochs,
        "Train Loss": np.clip(train_loss, 0.05, 3.0),
        "Validation Loss": np.clip(val_loss, 0.08, 3.0)
    }).set_index("Epoch")
    
    st.line_chart(chart_data)