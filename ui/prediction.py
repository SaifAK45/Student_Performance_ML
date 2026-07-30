import streamlit as st

from src.pipeline.predict_pipeline import PredictPipeline, CustomData


def show_prediction(user_data):
    """
    Predicts the student's math score
    and displays the results.
    """

    try:

        # -----------------------------
        # Create CustomData Object
        # -----------------------------
        custom_data = CustomData(
            gender=user_data["gender"],
            race_ethnicity=user_data["race_ethnicity"],
            parental_level_of_education=user_data["parental_level_of_education"],
            lunch=user_data["lunch"],
            test_preparation_course=user_data["test_preparation_course"],
            reading_score=user_data["reading_score"],
            writing_score=user_data["writing_score"]
        )

        pred_df = custom_data.get_data_as_dataframe()

        # -----------------------------
        # Predict
        # -----------------------------
        with st.spinner("Predicting..."):

            pipeline = PredictPipeline()

            prediction = pipeline.predict(pred_df)

            score = round(float(prediction[0]), 2)

        # -----------------------------
        # Student Details
        # -----------------------------
        with st.expander("📋 Student Details", expanded=False):

            st.dataframe(
                pred_df,
                hide_index=True,
                use_container_width=True
            )

        st.write("")

        # -----------------------------
        # Prediction Card
        # -----------------------------
        st.markdown(
            f"""
            <div class="prediction-card">
                <h5>🎯 Predicted Math Score</h5>
                <h4>{score}</h4>
            </div>
             """,
            unsafe_allow_html=True
        )

        st.write("")

        # -----------------------------
        # Grade
        # -----------------------------
        if score >= 90:
            grade = "A+"
            message = "🌟 Outstanding Performance!"
            status = "success"

        elif score >= 80:
            grade = "A"
            message = "🎉 Excellent Performance!"
            status = "success"

        elif score >= 70:
            grade = "B"
            message = "👍 Very Good Performance!"
            status = "info"

        elif score >= 60:
            grade = "C"
            message = "🙂 Good Performance!"
            status = "warning"

        elif score >= 40:
            grade = "D"
            message = "📚 Average Performance!"
            status = "warning"

        else:
            grade = "F"
            message = "❌ Needs Improvement!"
            status = "error"

        # -----------------------------
        # Metrics
        # -----------------------------
        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(
                "🎓 Score",
                score
            )

        with col2:
            st.metric(
                "🏆 Grade",
                grade
            )

        with col3:
            st.metric(
                "📈 Performance",
                f"{int(score)}%"
            )

        st.write("")

        # -----------------------------
        # Progress Bar
        # -----------------------------
        st.subheader("Performance")

        st.progress(min(int(score), 100))

        st.write("")

        # -----------------------------
        # Feedback
        # -----------------------------
        if status == "success":
            st.success(message)

            if score >= 90:
                st.balloons()

        elif status == "info":
            st.info(message)

        elif status == "warning":
            st.warning(message)

        else:
            st.error(message)

    except Exception as e:

        st.error("Prediction Failed")

        st.exception(e)