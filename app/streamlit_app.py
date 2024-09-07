import streamlit as st
from utils.model_loader import load_model
from utils.predictor import get_prediction

st.set_page_config("IRIS Prediction", page_icon="🌺")

st.title("IRIS Flower Prediction App")
st.markdown("---")

st.image("app/images/iris-flowers.jpg")
st.write("")

model = load_model("models/IRIS_Model.pkl")

col1, col2 = st.columns(2)

# Create two columns for input fields
col1, col2 = st.columns(2)

with col1:
    sepal_length = st.number_input(
        "Sepal Length (cm)", min_value=0.0, max_value=10.0, step=0.1, value=5.0
    )
    petal_length = st.number_input(
        "Petal Length (cm)", min_value=0.0, max_value=10.0, step=0.1, value=3.5
    )

with col2:
    sepal_width = st.number_input(
        "Sepal Width (cm)", min_value=0.0, max_value=10.0, step=0.1, value=1.3
    )
    petal_width = st.number_input(
        "Petal Width (cm)", min_value=0.0, max_value=10.0, step=0.1, value=0.2
    )


if st.button("Prediction"):
    data = [sepal_length, sepal_width, petal_length, petal_width]
    prediction = get_prediction(model, data)
    st.success(f"Predicted Species: {prediction}")
