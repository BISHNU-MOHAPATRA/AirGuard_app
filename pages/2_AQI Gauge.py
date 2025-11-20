import streamlit as st
import plotly.graph_objects as go
import random

st.set_page_config(layout="wide")

# ------------------------------------------------------------
# 🌿 PREMIUM UI (Glassmorphism + Glow + Animation)
# ------------------------------------------------------------
st.markdown("""
<style>
/* Center the gauge card */
.gauge-container {
    background: rgba(255, 255, 255, 0.55);
    backdrop-filter: blur(10px);
    padding: 25px;
    border-radius: 18px;
    box-shadow: 0px 4px 20px rgba(0,0,0,0.15);
    text-align: center;
    width: 90%;
    margin-left: auto;
    margin-right: auto;
    animation: fadeIn 0.8s ease-in-out;
}

/* AQI Status Box */
.aqi-box {
    padding: 12px;
    border-radius: 10px;
    font-size: 20px;
    font-weight: 600;
    margin-top: 10px;
    color: white;
}

/* Title animation */
@keyframes fadeIn {
    0% {opacity: 0; transform: translateY(12px);}
    100% {opacity: 1; transform: translateY(0);}
}
</style>
""", unsafe_allow_html=True)

# ------------------------------------------------------------
# 🌿 Title
# ------------------------------------------------------------
st.markdown("""
<h1 style='text-align:center; color:#1B5E20; font-weight:900;'>
🌿 AirGuard™ — AQI Gauge Meter
</h1>
""", unsafe_allow_html=True)

st.write(" ")

# ------------------------------------------------------------
# 💨 Generate random AQI (simulated)
# ------------------------------------------------------------
aqi_value = random.randint(10, 350)

# AQI Health Category
def get_aqi_status(aqi):
    if aqi <= 50:
        return "Good", "#4CAF50"
    elif aqi <= 100:
        return "Moderate", "#FFC107"
    elif aqi <= 150:
        return "Unhealthy for Sensitive Groups", "#FF9800"
    elif aqi <= 200:
        return "Unhealthy", "#F44336"
    elif aqi <= 300:
        return "Very Unhealthy", "#6A1B9A"
    else:
        return "Hazardous", "#4A148C"

status, color = get_aqi_status(aqi_value)

# ------------------------------------------------------------
# 🌡 AQI Gauge (Plotly)
# ------------------------------------------------------------
fig = go.Figure(go.Indicator(
    mode="gauge+number",
    value=aqi_value,
    title={'text': "Air Quality Index", 'font': {'size': 26}},
    gauge={
        'axis': {'range': [0, 500]},
        'bar': {'color': color},
        'borderwidth': 2,
        'bordercolor': "#1B5E20",
        'steps': [
            {'range': [0, 50], 'color': '#A5D6A7'},
            {'range': [51, 100], 'color': '#FFF59D'},
            {'range': [101, 150], 'color': '#FFCC80'},
            {'range': [151, 200], 'color': '#EF9A9A'},
            {'range': [201, 300], 'color': '#CE93D8'},
            {'range': [301, 500], 'color': '#B39DDB'},
        ],
    }
))

fig.update_layout(
    margin=dict(l=40, r=40, t=40, b=10),
    height=420,
)

# ------------------------------------------------------------
# 🌿 Display Gauge Inside Premium Card
# ------------------------------------------------------------
st.markdown("<div class='gauge-container'>", unsafe_allow_html=True)
st.plotly_chart(fig, use_container_width=True)

# AQI Status Box
st.markdown(
    f"<div class='aqi-box' style='background:{color};'>🌡 AQI Status: {status}</div>",
    unsafe_allow_html=True
)

st.markdown("</div>", unsafe_allow_html=True)