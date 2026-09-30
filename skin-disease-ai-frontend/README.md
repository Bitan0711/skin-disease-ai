# Skin Disease AI — Frontend

Streamlit frontend for a final-year B.Tech project on multiclass skin disease classification with a future Explainable AI component.

## Current scope

This repository currently contains **frontend/application code only**.

It does **not** implement:

- CNN training
- PyTorch inference
- Grad-CAM
- Dataset processing

The application currently uses a mock prediction provider so the interface can be developed before the trained model is ready.

## Run locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Folder structure

```text
skin-disease-ai/
├── app.py
├── assets/
├── components/
│   ├── upload.py
│   ├── prediction_card.py
│   ├── probability_chart.py
│   └── xai_panel.py
├── backend/
│   ├── model_loader.py
│   ├── preprocessing.py
│   └── predictor.py
├── xai/
│   ├── gradcam.py
│   └── visualization.py
├── models/
├── pages/
├── utils/
├── tests/
├── config.yaml
├── requirements.txt
└── .gitignore
```

## Future CNN connection

Keep the frontend interface unchanged.

Replace the mock implementation inside:

```text
backend/predictor.py
```

with the real PyTorch inference pipeline.

The frontend expects:

```python
{
    "predicted_class": str,
    "confidence": float,
    "probabilities": dict,
    "gradcam": image_or_none,
    "overlay": image_or_none,
    "mode": str,
}
```

The trained model can later be loaded through:

```text
backend/model_loader.py
```

For example:

```text
models/
└── model.pth
```

The exact model architecture and preprocessing must match the training code.

## Future XAI connection

Implement Grad-CAM separately in:

```text
xai/gradcam.py
```

The frontend already has display slots for:

1. Original image
2. Grad-CAM heatmap
3. Grad-CAM overlay

Once the XAI function returns compatible image objects, pass them into `render_xai_panel()`.

## Medical disclaimer

This application is a research and educational prototype. It is not intended to provide a medical diagnosis or replace evaluation by a qualified healthcare professional.
