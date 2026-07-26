# 🆔 Automated KYC Identity Card & Document Parser

A fine-tuned Vision-Language Model (`Qwen2-VL-2B-Instruct`) using **PyTorch**, **PEFT (QLoRA)**, and **BitsAndBytes 4-bit quantization** to parse unstructured identity documents into structured JSON with visual bounding box grounding.

---

## 🏗️ Architecture & Project Structure

```text
vlm-kyc-parser/
├── config/
│   ├── config.yaml          # Model hyperparameters & target modules
│   └── schema.py            # Pydantic schema for structured output
├── src/
│   ├── dataset.py           # Dataset processing pipeline
│   ├── model.py             # QLoRA injection & quantization setup
│   ├── train.py             # PyTorch training loop
│   └── evaluate.py          # ANLS & Exact Match evaluation metrics
├── app.py                   # Streamlit web UI with bounding box overlays
├── requirements.txt
└── README.md