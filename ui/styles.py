import streamlit as st


def load_css():
    """
    Loads all custom CSS for the application.
    """

    st.markdown(
        """
<style>

/*=====================================================
GLOBAL
=====================================================*/

#MainMenu{
    visibility:hidden;
}

header{
    visibility:hidden;
}

footer{
    visibility:hidden;
}

.block-container{
    padding-top:0.6rem;
    padding-bottom:1rem;
    padding-left:2rem;
    padding-right:2rem;
}

/*=====================================================
BACKGROUND
=====================================================*/

.stApp{

    background:linear-gradient(
        135deg,
        #0F172A,
        #111827,
        #1E293B
    );

}

/*=====================================================
SIDEBAR
=====================================================*/

[data-testid="stSidebar"]{

    background:#111827;
    border-right:1px solid #374151;

}

[data-testid="stSidebar"] h1{

    color:white;

}

[data-testid="stSidebar"] p{

    color:#CBD5E1;

}

/*=====================================================
HEADINGS
=====================================================*/

.main-title{

    font-size:52px;

    font-weight:700;

    color:white;

    text-align:center;

    margin-bottom:0;

}

.sub-title{

    text-align:center;

    color:#CBD5E1;

    font-size:18px;

    margin-top:0;

    margin-bottom:20px;

}

/*=====================================================
BUTTON
=====================================================*/

div.stButton > button{

    width:100%;

    height:55px;

    border:none;

    border-radius:12px;

    font-size:18px;

    font-weight:bold;

    color:white;

    background:linear-gradient(
        90deg,
        #2563EB,
        #4F46E5
    );

    transition:.3s;

}

div.stButton > button:hover{

    transform:translateY(-3px);

    box-shadow:0 8px 20px rgba(79,70,229,.45);

}

/*=====================================================
SELECT BOX
=====================================================*/

div[data-baseweb="select"]{

    border-radius:10px;

}

/*=====================================================
NUMBER INPUT
=====================================================*/

div[data-testid="stNumberInput"]{

    border-radius:10px;

}

/*=====================================================
SLIDER
=====================================================*/

div[data-testid="stSlider"]{

    padding-top:8px;

}

/*=====================================================
METRIC CARD
=====================================================*/

[data-testid="metric-container"]{

    background:#1F2937;

    border:1px solid #374151;

    border-radius:15px;

    padding:18px;

}

/*=====================================================
DATAFRAME
=====================================================*/

[data-testid="stDataFrame"]{

    border-radius:12px;

}

/*=====================================================
SUCCESS
=====================================================*/

div[data-testid="stAlert"]{

    border-radius:12px;

}

/*=====================================================
PROGRESS BAR
=====================================================*/

div[data-testid="stProgressBar"]{

    height:16px;

}

/*=====================================================
PREDICTION CARD
=====================================================*/

.prediction-card{

    background:linear-gradient(
        135deg,
        #2563EB,
        #4F46E5
    );

    border-radius:20px;

    padding:35px;

    text-align:center;

    color:white;

    box-shadow:0 12px 35px rgba(37,99,235,.35);

}

.prediction-card h2{

    margin:0;

    font-size:24px;

    font-weight:500;

}

.prediction-card h1{

    margin-top:18px;

    margin-bottom:0;

    font-size:58px;

    color:white;

}

/*=====================================================
FOOTER
=====================================================*/

.footer{

    text-align:center;

    color:#94A3B8;

    font-size:14px;

    margin-top:10px;

    padding-bottom:5px;

}

/*=====================================================
ANIMATION
=====================================================*/

@keyframes fadeIn{

    from{

        opacity:0;
        transform:translateY(15px);

    }

    to{

        opacity:1;
        transform:translateY(0);

    }

}

.prediction-card{

    animation:fadeIn .5s ease;

}

[data-testid="metric-container"]{

    animation:fadeIn .6s ease;

}

</style>
""",
        unsafe_allow_html=True,
    )