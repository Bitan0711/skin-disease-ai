"""
Future Grad-CAM integration point.

This file intentionally does not implement XAI.
Later, connect the trained PyTorch CNN here.
"""

def generate_gradcam(model, image, target_class=None):
    """
    Return a Grad-CAM heatmap image.

    Expected future return:
        PIL.Image / numpy array / compatible image object
    """
    return None


def generate_overlay(original_image, heatmap):
    """Return the Grad-CAM overlay in the future implementation."""
    return None
