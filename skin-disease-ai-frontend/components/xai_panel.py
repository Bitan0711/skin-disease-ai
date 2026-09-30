import io
import streamlit as st
from PIL import Image

def render_xai_panel(original_bytes=None, heatmap=None, overlay=None):
    st.subheader("Explainable AI")
    st.write(
        "The future Grad-CAM module will highlight image regions that "
        "contributed to the CNN prediction."
    )

    left, middle, right = st.columns(3)

    with left:
        st.markdown("**Original image**")
        if original_bytes:
            st.image(Image.open(io.BytesIO(original_bytes)), use_container_width=True)
        else:
            st.info("Original image will appear here.")

    with middle:
        st.markdown("**Grad-CAM heatmap**")
        if heatmap is not None:
            st.image(heatmap, use_container_width=True)
        else:
            st.info("Grad-CAM will appear here after XAI is connected.")

    with right:
        st.markdown("**Overlay**")
        if overlay is not None:
            st.image(overlay, use_container_width=True)
        else:
            st.info("Grad-CAM overlay will appear here later.")

    st.caption(
        "A Grad-CAM visualization represents regions that influenced the "
        "model's prediction; it is not a clinically verified lesion boundary."
    )
