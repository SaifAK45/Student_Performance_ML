import streamlit as st


def show_form():
    """
    Displays the student input form and
    returns all user inputs.
    """

    st.subheader("📝 Student Information")

    with st.container(border=True):

        col1, col2 = st.columns(2)

        # -----------------------------
        # LEFT COLUMN
        # -----------------------------
        with col1:

            gender = st.selectbox(
                "Gender",
                (
                    "male",
                    "female"
                )
            )

            race_ethnicity = st.selectbox(
                "Race / Ethnicity",
                (
                    "group A",
                    "group B",
                    "group C",
                    "group D",
                    "group E"
                )
            )

            parental_level_of_education = st.selectbox(
                "Parental Level of Education",
                (
                    "associate's degree",
                    "bachelor's degree",
                    "high school",
                    "master's degree",
                    "some college",
                    "some high school"
                )
            )

            lunch = st.selectbox(
                "Lunch Type",
                (
                    "standard",
                    "free/reduced"
                )
            )

        # -----------------------------
        # RIGHT COLUMN
        # -----------------------------
        with col2:

            test_preparation_course = st.selectbox(
                "Test Preparation Course",
                (
                    "none",
                    "completed"
                )
            )

            reading_score = st.slider(
                "Reading Score",
                min_value=0,
                max_value=100,
                value=70
            )

            writing_score = st.slider(
                "Writing Score",
                min_value=0,
                max_value=100,
                value=70
            )

        st.write("")

        predict_button = st.button(
            "🚀 Predict Math Score",
            use_container_width=True
        )

    # -----------------------------------
    # Return values only when button pressed
    # -----------------------------------

    if predict_button:

        return {
            "gender": gender,
            "race_ethnicity": race_ethnicity,
            "parental_level_of_education": parental_level_of_education,
            "lunch": lunch,
            "test_preparation_course": test_preparation_course,
            "reading_score": reading_score,
            "writing_score": writing_score
        }

    return None