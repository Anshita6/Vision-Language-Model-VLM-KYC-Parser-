import numpy as np

def calculate_iou(boxA, boxB):
    """
    Calculates Intersection over Union (IoU) for predicted vs ground-truth
    normalized coordinates: [ymin, xmin, ymax, xmax]
    """
    yA = max(boxA[0], boxB[0])
    xA = max(boxA[1], boxB[1])
    yB = min(boxA[2], boxB[2])
    xB = min(boxA[3], boxB[3])

    interArea = max(0, xB - xA) * max(0, yB - yA)
    boxAArea = (boxA[2] - boxA[0]) * (boxA[3] - boxA[1])
    boxBArea = (boxB[2] - boxB[0]) * (boxB[3] - boxB[1])

    iou = interArea / float(boxAArea + boxBArea - interArea + 1e-6)
    return round(float(iou), 4)

def evaluate_predictions(predictions, ground_truths):
    """Computes Mean IoU across normalized coordinate targets."""
    ious = []
    for pred_bbox, gt_bbox in zip(predictions, ground_truths):
        ious.append(calculate_iou(pred_bbox, gt_bbox))
    return {
        "mean_iou": round(float(np.mean(ious)), 4),
        "exact_match_ratio": round(float(np.mean([i > 0.85 for i in ious])), 4)
    }