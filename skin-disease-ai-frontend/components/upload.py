import streamlit as st

def render_upload():
    """Render the image uploader and return the uploaded file."""
    st.subheader("Upload skin image")
    st.caption("Supported formats: JPG, JPEG, PNG")

    uploaded_file = st.file_uploader(
        "Choose an image",
        type=["jpg", "jpeg", "png"],
        label_visibility="collapsed",
    )

    if uploaded_file:
        st.image(
            uploaded_file,
            caption=uploaded_file.name,
            width=420,
        )

    return uploaded_file
