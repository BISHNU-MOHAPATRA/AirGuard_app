<<<<<<< HEAD
import streamlit as st
import numpy as np
import joblib

st.markdown("""
<div style="
    background: linear-gradient(90deg, #1B5E20, #66BB6A);
    padding: 15px;
    border-radius: 10px;
    text-align:center;
    color:white;
    font-size:24px;
    font-weight:800;
    margin-bottom:20px;">
🌿 AirGuard™ — AI AQI Prediction
</div>
""", unsafe_allow_html=True)


# ---------------------------------------------
# Load Model Safely
# ---------------------------------------------
model_path = "aqi_model.pkl"
model = joblib.load(model_path)


# ---------------------------------------------
# Page Title
# ---------------------------------------------
st.markdown("<h2 style='text-align:center;'>📡 Enter Sensor Readings</h2>", unsafe_allow_html=True)
st.write(" ")


# ---------------------------------------------
# Input Fields (3 Columns Layout)
# ---------------------------------------------
col1, col2, col3 = st.columns(3)

with col1:
    pm25 = st.number_input("PM2.5 (µg/m³)", 0, 500, 55)
    temp = st.number_input("Temperature (°C)", -10, 60, 30)

with col2:
    pm10 = st.number_input("PM10 (µg/m³)", 0, 600, 80)
    humidity = st.number_input("Humidity (%)", 0, 100, 50)

with col3:
    co = st.number_input("CO (mg/m³)", 0.0, 20.0, 1.0)
    no2 = st.number_input("NO₂ (µg/m³)", 0, 400, 40)


st.write(" ")
predict_btn = st.button("➤ Predict AQI", use_container_width=True)
st.write(" ")


# ---------------------------------------------
# Prediction Logic + Premium Output
# ---------------------------------------------
if predict_btn:

    # Prepare input
    data = np.array([[pm25, pm10, co, no2, temp, humidity]])
    pred = model.predict(data)[0]
    aqi = int(pred)   # FIXED: now AQI exists

    # Decide Category + Color + Advice
    if aqi <= 50:
        category = "Good"
        color = "#4CAF50"
        advice = "Air quality is satisfactory and poses little or no risk."
    elif aqi <= 100:
        category = "Moderate"
        color = "#FFEB3B"
        advice = "Acceptable air quality. Sensitive individuals should reduce exertion."
    elif aqi <= 150:
        category = "Unhealthy for Sensitive Groups"
        color = "#FF9800"
        advice = "People with breathing issues should reduce prolonged outdoor activity."
    elif aqi <= 200:
        category = "Unhealthy"
        color = "#F44336"
        advice = "Everyone may experience health effects. Avoid outdoor exposure."
    elif aqi <= 300:
        category = "Very Unhealthy"
        color = "#6A1B9A"
        advice = "Health warnings issued. Stay indoors as much as possible."
    else:
        category = "Hazardous"
        color = "#4A0000"
        advice = "Serious health effects. Avoid going outdoors entirely."

    # ---------------------------------------------
    # Premium AQI Output Card
    # ---------------------------------------------
    st.markdown(f"""
    <div style="
        background:{color};
        padding:22px;
        border-radius:12px;
        text-align:center;
        color:white;
        font-size:26px;
        font-weight:800;
        box-shadow:0px 4px 12px rgba(0,0,0,0.2);
        ">
        ➤ Predicted AQI: {aqi} <br>
        <span style="font-size:22px; font-weight:600;">{category}</span>
    </div>
    """, unsafe_allow_html=True)

    st.write(" ")

    # ---------------------------------------------
    # Premium Health Advice Box
    # ---------------------------------------------
    st.markdown(f"""
    <div style="
        border-left:6px solid {color};
        background:#FFF8C6;
        padding:16px;
        border-radius:10px;
        font-size:18px;
        box-shadow:0px 3px 10px rgba(0,0,0,0.1);
    ">
        <b>💡 Health Advice</b><br>{advice}
    </div>
=======
import streamlit as st
import numpy as np
import joblib

st.markdown("""
<div style="
    background: linear-gradient(90deg, #1B5E20, #66BB6A);
    padding: 15px;
    border-radius: 10px;
    text-align:center;
    color:white;
    font-size:24px;
    font-weight:800;
    margin-bottom:20px;">
🌿 AirGuard™ — AI AQI Prediction
</div>
""", unsafe_allow_html=True)


# ---------------------------------------------
# Load Model Safely
# ---------------------------------------------
model_path = "aqi_model.pkl"
model = joblib.load(model_path)


# ---------------------------------------------
# Page Title
# ---------------------------------------------
st.markdown("<h2 style='text-align:center;'>📡 Enter Sensor Readings</h2>", unsafe_allow_html=True)
st.write(" ")


# ---------------------------------------------
# Input Fields (3 Columns Layout)
# ---------------------------------------------
col1, col2, col3 = st.columns(3)

with col1:
    pm25 = st.number_input("PM2.5 (µg/m³)", 0, 500, 55)
    temp = st.number_input("Temperature (°C)", -10, 60, 30)

with col2:
    pm10 = st.number_input("PM10 (µg/m³)", 0, 600, 80)
    humidity = st.number_input("Humidity (%)", 0, 100, 50)

with col3:
    co = st.number_input("CO (mg/m³)", 0.0, 20.0, 1.0)
    no2 = st.number_input("NO₂ (µg/m³)", 0, 400, 40)


st.write(" ")
predict_btn = st.button("➤ Predict AQI", use_container_width=True)
st.write(" ")


# ---------------------------------------------
# Prediction Logic + Premium Output
# ---------------------------------------------
if predict_btn:

    # Prepare input
    data = np.array([[pm25, pm10, co, no2, temp, humidity]])
    pred = model.predict(data)[0]
    aqi = int(pred)   # FIXED: now AQI exists

    # Decide Category + Color + Advice
    if aqi <= 50:
        category = "Good"
        color = "#4CAF50"
        advice = "Air quality is satisfactory and poses little or no risk."
    elif aqi <= 100:
        category = "Moderate"
        color = "#FFEB3B"
        advice = "Acceptable air quality. Sensitive individuals should reduce exertion."
    elif aqi <= 150:
        category = "Unhealthy for Sensitive Groups"
        color = "#FF9800"
        advice = "People with breathing issues should reduce prolonged outdoor activity."
    elif aqi <= 200:
        category = "Unhealthy"
        color = "#F44336"
        advice = "Everyone may experience health effects. Avoid outdoor exposure."
    elif aqi <= 300:
        category = "Very Unhealthy"
        color = "#6A1B9A"
        advice = "Health warnings issued. Stay indoors as much as possible."
    else:
        category = "Hazardous"
        color = "#4A0000"
        advice = "Serious health effects. Avoid going outdoors entirely."

    # ---------------------------------------------
    # Premium AQI Output Card
    # ---------------------------------------------
    st.markdown(f"""
    <div style="
        background:{color};
        padding:22px;
        border-radius:12px;
        text-align:center;
        color:white;
        font-size:26px;
        font-weight:800;
        box-shadow:0px 4px 12px rgba(0,0,0,0.2);
        ">
        ➤ Predicted AQI: {aqi} <br>
        <span style="font-size:22px; font-weight:600;">{category}</span>
    </div>
    """, unsafe_allow_html=True)

    st.write(" ")

    # ---------------------------------------------
    # Premium Health Advice Box
    # ---------------------------------------------
    st.markdown(f"""
    <div style="
        border-left:6px solid {color};
        background:#FFF8C6;
        padding:16px;
        border-radius:10px;
        font-size:18px;
        box-shadow:0px 3px 10px rgba(0,0,0,0.1);
    ">
        <b>💡 Health Advice</b><br>{advice}
    </div>
>>>>>>> dcaf2231992952bf1ed21ab181fc1543d04f3185
    """, unsafe_allow_html=True)