import torch
from torch.utils.data import Dataset
from PIL import Image

class KYCVisualGroundingDataset(Dataset):
    """
    Custom PyTorch Dataset for normalizing document images and mapping text target labels
    to normalized bounding box coordinates [ymin, xmin, ymax, xmax] in 0..1000 space.
    """
    def __init__(self, data_samples, image_processor, tokenizer, max_length=512):
        self.samples = data_samples
        self.image_processor = image_processor
        self.tokenizer = tokenizer
        self.max_length = max_length

    def __len__(self):
        return len(self.samples)

    def normalize_bbox(self, bbox, width, height):
        """Normalizes pixel coordinates [x1, y1, x2, y2] into [0, 1000] space."""
        x1, y1, x2, y2 = bbox
        return [
            int(1000 * (y1 / height)),
            int(1000 * (x1 / width)),
            int(1000 * (y2 / height)),
            int(1000 * (x2 / width))
        ]

    def __getitem__(self, idx):
        item = self.samples[idx]
        image = Image.open(item["image_path"]).convert("RGB")
        w, h = image.size

        # Preprocess visual tensor
        pixel_values = self.image_processor(image, return_tensors="pt").pixel_values.squeeze(0)

        # Normalize target bounding boxes
        normalized_fields = {}
        for field_name, meta in item["fields"].items():
            normalized_fields[field_name] = {
                "value": meta["value"],
                "bbox": self.normalize_bbox(meta["bbox_pixels"], w, h)
            }

        prompt = f"<grounding> Extract fields for document type: {item['doc_type']}"
        target_json = str(normalized_fields)

        inputs = self.tokenizer(
            prompt,
            max_length=self.max_length,
            padding="max_length",
            truncation=True,
            return_tensors="pt"
        )

        labels = self.tokenizer(
            target_json,
            max_length=self.max_length,
            padding="max_length",
            truncation=True,
            return_tensors="pt"
        ).input_ids

        return {
            "pixel_values": pixel_values,
            "input_ids": inputs.input_ids.squeeze(0),
            "attention_mask": inputs.attention_mask.squeeze(0),
            "labels": labels.squeeze(0)
        }