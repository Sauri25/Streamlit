import streamlit as st
import joblib
import numpy as np

# Load model
model = joblib.load("salary_model.pkl")

# Custom CSS for style
st.markdown(
    """
    <style>
        .main {
            background-color: #f5f7fa;
        }
        .stApp {
            background: linear-gradient(to right, #e0f7fa, #ffffff);
            color: #333333;
            font-family: 'Segoe UI', sans-serif;
        }
        .title {
            font-size: 2.5em;
            color: #1a73e8;
            text-align: center;
        }
        .subtitle {
            font-size: 1.2em;
            color: #555;
            text-align: center;
        }
        .predict-button {
            background-color: #1a73e8;
            color: white;
            font-size: 18px;
            padding: 10px 20px;
            border-radius: 10px;
        }
        .result-card {
            background-color: #e3f2fd;
            border-left: 6px solid #1a73e8;
            padding: 20px;
            border-radius: 10px;
            margin-top: 20px;
        }
    </style>
""",
    unsafe_allow_html=True,
)

# Title
st.markdown(
    "<div class='title'>💼 AI-Powered Salary Predictor</div>", unsafe_allow_html=True
)
st.markdown(
    "<div class='subtitle'>Estimate your salary based on experience</div>",
    unsafe_allow_html=True,
)
st.markdown("---")

# Input area
st.subheader("📥 Enter Your Experience")
col1, col2 = st.columns([1, 2])
with col1:
    experience = st.slider("Years of Experience", 0.0, 30.0, 1.0, 0.1)
with col2:
    st.write("Or type below 👇")
    exp_input = st.number_input(
        "Type experience:", min_value=0.0, max_value=50.0, value=experience, step=0.1
    )
    if exp_input != experience:
        experience = exp_input

# Predict
if st.button("🚀 Predict Salary"):
    input_data = np.array([[experience]])
    prediction = model.predict(input_data)[0]

    st.markdown(
        f"""
    <div class='result-card'>
        <h3>🔍 Prediction Result:</h3>
        <p><strong>Experience:</strong> {experience:.1f} years</p>
        <p><strong>Estimated Salary:</strong> ₹ {prediction:,.2f}</p>
    </div>
    """,
        unsafe_allow_html=True,
    )

    st.balloons()

# Footer
st.markdown("---")
st.caption(
    "👨‍💻 Built by Saurav Raj Aryal | 🔧 Model: Linear Regression | 📦 File: salary_model.pkl"
)
