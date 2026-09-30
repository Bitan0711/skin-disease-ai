import streamlit as st

def render_prediction_card(result):
    st.subheader("Prediction")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Detected condition", result["predicted_class"])

    with col2:
        st.metric("Confidence", f'{result["confidence"] * 100:.1f}%')

    with col3:
        mode = "Demo" if result.get("mode") == "demo" else "Model"
        st.metric("Inference mode", mode)

    if result.get("mode") == "demo":
        st.info(
            "This is placeholder output. Connect your trained PyTorch CNN "
            "through backend/predictor.py when the model is ready."
        )
