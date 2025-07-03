import streamlit as st
import requests

st.set_page_config(page_title="Seattle Weather Classifier", page_icon="⛅")
st.title("🌤️ Weather Classifier")

st.markdown("Enter the weather measurements below:")

# Input widgets
precipitation = st.number_input("Precipitation (mm)", min_value=0.0, step=0.1)
temp_max = st.number_input("Max Temperature (°C)", step=0.1)
temp_min = st.number_input("Min Temperature (°C)", step=0.1)
wind = st.number_input("Wind Speed (units)", min_value=0.0, step=0.1)

# Prediction button
if st.button("Predict Weather"):
    input_data = {
        "precipitation": precipitation,
        "temp_max": temp_max,
        "temp_min": temp_min,
        "wind": wind
    }

    try:
        # Make API call
        response = requests.post("http://127.0.0.1:5000/predict", json=input_data)
        if response.status_code == 200:
            prediction = response.json()["prediction"]
            st.success(f"🌈 Predicted Weather: **{prediction.upper()}**")
        else:
            st.error(f"❌ Error: {response.json().get('error', 'Unknown error')}")
    except requests.exceptions.ConnectionError:
        st.error("⚠️ Could not connect to the Flask API. Make sure it's running on http://127.0.0.1:5000.")
