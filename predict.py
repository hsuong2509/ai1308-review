THRESHOLD = 0.5


def predict(scores):
    """Nhãn có điểm cao nhất trong dict {nhãn: điểm}."""
    label = max(scores, key=scores.get)
    return label if scores[label] >= THRESHOLD else "unknown"
