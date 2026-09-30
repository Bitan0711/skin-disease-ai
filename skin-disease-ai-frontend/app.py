import streamlit as st
from pathlib import Path
from backend.predictor import predict
from components.xai_panel import render_xai_panel
from components.prediction_card import render_prediction_card
from components.probability_chart import render_probability_chart
from components.upload import render_upload

st.set_page_config(
    page_title="Skin Disease AI",
    page_icon="🩺",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ---------- Theme ----------
if "theme" not in st.session_state:
    st.session_state.theme = "light"

with st.sidebar:
    st.markdown("## 🩺 Skin Disease AI")
    st.caption("Deep Learning + Explainable AI")
    st.divider()

    page = st.radio(
        "Navigation",
        ["Home", "Disease Prediction", "About"],
        label_visibility="collapsed",
    )

    st.divider()
    theme = st.toggle(
        "Dark mode",
        value=st.session_state.theme == "dark",
    )
    st.session_state.theme = "dark" if theme else "light"

    st.caption("Research & educational prototype")

# ---------- CSS ----------
dark = st.session_state.theme == "dark"
bg = "#10161d" if dark else "#f5f7fa"
card = "#18212b" if dark else "#ffffff"
text = "#edf2f7" if dark else "#17202a"
muted = "#a9b4c0" if dark else "#5d6875"
border = "#2b3744" if dark else "#dfe5eb"
primary = "#4f9da6"

st.markdown(
    f"""
    <style>
    .stApp {{
        background: {bg};
        color: {text};
    }}
    .block-container {{
        max-width: 1180px;
        padding-top: 2rem;
        padding-bottom: 3rem;
    }}
    .hero {{
        padding: 2.2rem;
        border: 1px solid {border};
        border-radius: 18px;
        background: {card};
        margin-bottom: 1.5rem;
    }}
    .hero h1 {{
        margin: 0;
        font-size: 2.6rem;
        letter-spacing: -0.04em;
        color: {text};
    }}
    .hero p {{
        color: {muted};
        font-size: 1.05rem;
        margin-top: .65rem;
    }}
    .section-card {{
        padding: 1.3rem;
        border: 1px solid {border};
        border-radius: 15px;
        background: {card};
    }}
    .eyebrow {{
        color: {primary};
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: .08em;
        font-size: .75rem;
    }}
    .disclaimer {{
        color: {muted};
        font-size: .78rem;
        border-top: 1px solid {border};
        padding-top: 1rem;
        margin-top: 2rem;
    }}
    </style>
    """,
    unsafe_allow_html=True,
)

def footer():
    st.markdown(
        '<div class="disclaimer">'
        "Research and educational prototype. This application is not intended "
        "to provide a medical diagnosis or replace professional medical advice."
        "</div>",
        unsafe_allow_html=True,
    )

# ---------- Pages ----------
if page == "Home":
    st.markdown(
        '<div class="hero">'
        '<div class="eyebrow">Deep Learning Research Prototype</div>'
        '<h1>Skin Disease AI</h1>'
        '<p>Multiclass skin disease classification with a future '
        "Explainable AI integration.</p>"
        "</div>",
        unsafe_allow_html=True,
    )

    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown("### 01 · Upload")
        st.write("Provide a skin image for analysis.")
    with c2:
        st.markdown("### 02 · Classify")
        st.write("A future PyTorch CNN will provide the prediction.")
    with c3:
        st.markdown("### 03 · Explain")
        st.write("A future Grad-CAM module will visualize influential regions.")

    st.divider()
    st.subheader("Project workflow")
    st.write("Image → Preprocessing → CNN → Prediction → Grad-CAM → Explanation")

    footer()

elif page == "Disease Prediction":
    st.markdown(
        '<div class="hero">'
        '<div class="eyebrow">Analysis</div>'
        '<h1>Disease Prediction</h1>'
        '<p>Upload an image and analyze it using the future trained model.</p>'
        "</div>",
        unsafe_allow_html=True,
    )

    uploaded_file = render_upload()

    if uploaded_file is not None:
        if st.button("Analyze Image", type="primary", use_container_width=True):
            with st.spinner("Analyzing image..."):
                result = predict(uploaded_file)

            st.session_state.result = result
            st.session_state.uploaded_file = uploaded_file.getvalue()

    result = st.session_state.get("result")

    if result:
        st.divider()
        render_prediction_card(result)
        render_probability_chart(result["probabilities"])

        st.divider()
        render_xai_panel(
            original_bytes=st.session_state.get("uploaded_file"),
            heatmap=result.get("gradcam"),
            overlay=result.get("overlay"),
        )

    footer()

else:
    st.markdown(
        '<div class="hero">'
        '<div class="eyebrow">About</div>'
        '<h1>About the Project</h1>'
        '<p>Indian-focused skin disease classification using deep learning '
        "with an Explainable AI component.</p>"
        "</div>",
        unsafe_allow_html=True,
    )

    st.subheader("Technology")
    st.write(
        "The planned system uses Python, PyTorch and transfer-learning CNNs. "
        "The final application will connect the trained model to this interface "
        "and use Grad-CAM for visual explanations."
    )

    st.subheader("Future model connection")
    st.code(
        """image
  ↓
backend/preprocessing.py
  ↓
backend/model_loader.py
  ↓
backend/predictor.py
  ↓
prediction + probabilities
  ↓
xai/gradcam.py
  ↓
Streamlit UI""",
        language="text",
    )

    footer()
