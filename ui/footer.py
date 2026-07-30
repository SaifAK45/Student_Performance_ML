import streamlit as st


def show_footer():
    """
    Displays the application footer.
    """

    st.divider()

    st.markdown(
        """
<div class="footer">

Made with ❤️ by <b>Saif Ali Khan</b>

<br>

Student Performance Prediction using Machine Learning

<br>

Python • Streamlit • Scikit-Learn • Pandas

</div>
        """,
        unsafe_allow_html=True,
    )