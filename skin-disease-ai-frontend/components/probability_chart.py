import pandas as pd
import streamlit as st

def render_probability_chart(probabilities):
    st.subheader("Class probability distribution")

    df = pd.DataFrame(
        {
            "Disease": list(probabilities.keys()),
            "Probability": [
                value * 100 for value in probabilities.values()
            ],
        }
    ).set_index("Disease")

    st.bar_chart(df)
