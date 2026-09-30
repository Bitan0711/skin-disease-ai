"""
Prediction interface.

The frontend talks to this file instead of directly talking to the CNN.
Later, replace the mock implementation with real PyTorch inference.
"""

from backend.model_loader import load_model
from backend.preprocessing import preprocess_image


DEMO_PROBABILITIES = {
    "Psoriasis": 0.874,
    "Eczema": 0.052,
    "Vitiligo": 0.031,
    "Fungal Infection": 0.024,
    "Other": 0.019,
}


def predict(uploaded_file):
    """
    Return the stable result format expected by the frontend.

    Future real implementation:
        image -> preprocessing -> PyTorch model -> probabilities
    """
    image = uploaded_file
    _ = preprocess_image(image)
    _ = load_model()

    predicted_class = max(DEMO_PROBABILITIES, key=DEMO_PROBABILITIES.get)
    confidence = DEMO_PROBABILITIES[predicted_class]

    return {
        "predicted_class": predicted_class,
        "confidence": confidence,
        "probabilities": DEMO_PROBABILITIES,
        "gradcam": None,
        "overlay": None,
        "mode": "demo",
    }
