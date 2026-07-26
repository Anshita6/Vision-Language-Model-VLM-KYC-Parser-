import yaml
import torch
from transformers import TrainingArguments, Trainer
from src.model import load_peft_vlm
from src.dataset import load_kyc_dataset

def run_training():
    with open("config/config.yaml", "r") as f:
        config = yaml.safe_load(f)

    # 1. Load Model and Processor
    model, processor = load_peft_vlm(
        model_id=config["model"]["name"],
        lora_r=config["lora"]["r"],
        lora_alpha=config["lora"]["alpha"]
    )

    # 2. Load Dataset
    dataset = load_kyc_dataset(config["training"]["dataset_name"])

    # 3. Configure PyTorch Training Arguments
    training_args = TrainingArguments(
        output_dir=config["training"]["output_dir"],
        per_device_train_batch_size=config["training"]["batch_size"],
        gradient_accumulation_steps=4,
        learning_rate=float(config["training"]["learning_rate"]),
        num_train_epochs=config["training"]["epochs"],
        logging_steps=10,
        save_strategy="epoch",
        fp16=True,
        report_to="none"
    )

    # 4. Initialize Trainer
    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=dataset["train"],
        eval_dataset=dataset["validation"]
    )

    print("--> Starting QLoRA Fine-Tuning Execution...")
    trainer.train()

    print("--> Saving LoRA Adapter Weights...")
    model.save_pretrained("./outputs/adapters/")
    processor.save_pretrained("./outputs/adapters/")
    print("--> Training complete. Adapters saved to ./outputs/adapters/")

if __name__ == "__main__":
    run_training()