import streamlit as st


def show_sidebar():
    """
    Displays the application sidebar.
    """

    with st.sidebar:

        # ----------------------------
        # Logo
        # ----------------------------

        st.image(
            "https://img.icons8.com/color/96/graduation-cap.png",
            width=90
        )

        st.title("Student Performance")

        st.caption("Machine Learning Predictor")

        st.divider()

        # ----------------------------
        # About
        # ----------------------------

        st.subheader("📌 About")

        st.write(
            """
Predict a student's **Math Score**
using a trained Machine Learning model.

The prediction is based on
academic and demographic features.
            """
        )

        st.divider()

        # ----------------------------
        # Features
        # ----------------------------

        st.subheader("🚀 Features")

        features = [
            "Gender",
            "Race / Ethnicity",
            "Parental Education",
            "Lunch Type",
            "Test Preparation",
            "Reading Score",
            "Writing Score"
        ]

        for feature in features:
            st.markdown(f"✅ {feature}")

        st.divider()

        # ----------------------------
        # Model Information
        # ----------------------------

        st.subheader("🤖 Machine Learning Model")

        st.info(
            """
Regression Model

• Scikit-Learn

• Data Preprocessing

• Feature Engineering

• Pipeline Based Prediction
            """
        )

        st.divider()

        # ----------------------------
        # Tech Stack
        # ----------------------------

        st.subheader("🛠 Tech Stack")

        col1, col2 = st.columns(2)

        with col1:

            st.markdown("""
- Python
- Pandas
- NumPy
""")

        with col2:

            st.markdown("""
- Streamlit
- Scikit-Learn
- Pickle
""")

        st.divider()

        # ----------------------------
        # Developer
        # ----------------------------

        st.subheader("👨‍💻 Developer")

        st.success(
            """
Saif Ali Khan

AI & ML Engineer

Python | Machine Learning | Data Science
            """
        )