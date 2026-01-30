import streamlit as st
import pandas as pd
import pickle
# Page Config
st.set_page_config(page_title="Diamond Price Predictor", layout="centered")

st.title("💎 Diamond Price Prediction")
st.write("Predict diamond price using KNN Regression Model")

# Load Model

@st.cache_resource
def load_model():
    with open("diamond_knn_model.pkl", "rb") as f:
        return pickle.load(f)

model = load_model()

# User Inputs

st.subheader("Enter Diamond Details")

col1, col2 = st.columns(2)

with col1:
    carat = st.number_input("Carat", min_value=0.1, max_value=5.0, value=1.0)
    depth = st.number_input("Depth", min_value=40.0, max_value=80.0, value=60.0)
    table = st.number_input("Table", min_value=40.0, max_value=80.0, value=55.0)
    x = st.number_input("Length (x)", min_value=0.0, max_value=10.0, value=5.0)

with col2:
    y = st.number_input("Width (y)", min_value=0.0, max_value=10.0, value=5.0)
    z = st.number_input("Height (z)", min_value=0.0, max_value=10.0, value=3.0)
    cut = st.selectbox("Cut", ["Fair", "Good", "Very Good", "Premium", "Ideal"])
    color = st.selectbox("Color", ["D", "E", "F", "G", "H", "I", "J"])
    clarity = st.selectbox(
        "Clarity",
        ["I1", "SI2", "SI1", "VS2", "VS1", "VVS2", "VVS1", "IF"]
    )

# Prediction

if st.button("Predict Price 💰"):

    input_df = pd.DataFrame({
        "carat": [carat],
        "cut": [cut],
        "color": [color],
        "clarity": [clarity],
        "depth": [depth],
        "table": [table],
        "x": [x],
        "y": [y],
        "z": [z]
    })

    prediction = model.predict(input_df)[0]

    st.success(f"### 💵 Predicted Price: ${round(prediction, 2)}")

# Footer

st.markdown("---")
st.caption("Built with ❤️ using Streamlit + Scikit-learn")