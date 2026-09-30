# Future CNN Integration

The frontend deliberately does not contain CNN code.

## Connection point

Use:

```text
backend/model_loader.py
backend/preprocessing.py
backend/predictor.py
```

The eventual flow should be:

```text
Uploaded image
    ↓
preprocessing.py
    ↓
model_loader.py
    ↓
PyTorch CNN
    ↓
class probabilities
    ↓
predictor.py
    ↓
Streamlit
```

The predictor should return:

```python
{
    "predicted_class": "...",
    "confidence": 0.0,
    "probabilities": {
        "class_a": 0.0,
        "class_b": 0.0,
    },
    "gradcam": None,
    "overlay": None,
    "mode": "model",
}
```

Do not put CNN training code into the frontend repository unless it is intentionally added later.
