# Future XAI Integration

The frontend does not implement Grad-CAM.

Implement the future XAI logic in:

```text
xai/gradcam.py
```

Expected conceptual flow:

```text
Uploaded image
    ↓
trained PyTorch CNN
    ↓
target convolutional layer
    ↓
Grad-CAM
    ↓
heatmap
    ↓
overlay
    ↓
Streamlit
```

The prediction response already reserves:

```python
"gradcam": None,
"overlay": None,
```

Replace these with the generated images when the XAI implementation is ready.
