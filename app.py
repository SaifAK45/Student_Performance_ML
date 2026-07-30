import streamlit as st

from ui.styles import load_css
from ui.sidebar import show_sidebar
from ui.form import show_form
from ui.prediction import show_prediction
from ui.footer import show_footer


# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Student Performance Predictor",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -----------------------------
# Load CSS
# -----------------------------
load_css()

# -----------------------------
# Sidebar
# -----------------------------
show_sidebar()

# -----------------------------
# Title
# -----------------------------
st.markdown(
    """
    <div class="main-title">
        🎓 Student Performance Prediction
    </div>

    <div class="sub-title">
        Predict Math Score using Machine Learning
    </div>
    """,
    unsafe_allow_html=True
)

# -----------------------------
# Input Form
# -----------------------------
user_data = show_form()

# -----------------------------
# Prediction
# -----------------------------
if user_data:
    show_prediction(user_data)

# -----------------------------
# Footer
# -----------------------------
show_footer()