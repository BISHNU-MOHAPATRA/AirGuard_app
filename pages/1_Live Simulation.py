<<<<<<< HEAD
import streamlit as st
import numpy as np
import time

st.set_page_config(layout="wide")

# ------------------------------------------------------------
# 🌿 PREMIUM UI (Glassmorphism + Card Glow + Animation)
# ------------------------------------------------------------
st.markdown("""
<style>

.live-card {
    background: rgba(255, 255, 255, 0.55);
    backdrop-filter: blur(10px);
    padding: 22px;
    border-radius: 18px;
    box-shadow: 0px 4px 20px rgba(0,0,0,0.15);
    transition: 0.25s ease-in-out;
    text-align: center;
}

.live-card:hover {
    transform: scale(1.02);
    box-shadow: 0px 6px 25px rgba(0,0,0,0.20);
}

.sensor-value {
    font-size: 40px;
    font-weight: 900;
    color: #1B5E20;
}

.label {
    font-size: 20px;
    font-weight: 600;
    color: #555;
}

@keyframes fadeIn {
    0% {opacity: 0; transform: translateY(12px);}
    100% {opacity: 1; transform: translateY(0);}
}

</style>
""", unsafe_allow_html=True)


# ------------------------------------------------------------
# 🌿 HEADER
# ------------------------------------------------------------
st.markdown("""
<h1 style='text-align:center; color:#1B5E20; font-weight:900; animation:fadeIn 0.8s;'>
🚀 Live Pollution Sensor Simulation
</h1>
""", unsafe_allow_html=True)

st.write(" ")
st.write("---")
st.write(" ")

# ------------------------------------------------------------
# 🌿 Live Simulation Function
# ------------------------------------------------------------
def generate_sensor_data():
    return {
        "PM2.5": np.random.randint(10, 300),
        "PM10": np.random.randint(20, 400),
        "CO": round(np.random.uniform(0.1, 5.0), 2),
        "NO2": np.random.randint(5, 200),
        "Temperature": round(np.random.uniform(18, 40), 1),
        "Humidity": np.random.randint(20, 90)
    }


# ------------------------------------------------------------
# 🌿 BUTTON TO START SIMULATION
# ------------------------------------------------------------
start = st.button("🔄 Start Live Simulation", type="primary")

placeholder = st.empty()

if start:
    for i in range(30):
        data = generate_sensor_data()

        with placeholder.container():
            # Row layout
            col1, col2, col3 = st.columns(3)

            with col1:
                st.markdown(f"""
                <div class='live-card'>
                    <div class='label'>PM2.5</div>
                    <div class='sensor-value'>{data['PM2.5']}</div>
                </div>
                """, unsafe_allow_html=True)

                st.markdown(f"""
                <div class='live-card'>
                    <div class='label'>CO (ppm)</div>
                    <div class='sensor-value'>{data['CO']}</div>
                </div>
                """, unsafe_allow_html=True)

            with col2:
                st.markdown(f"""
                <div class='live-card'>
                    <div class='label'>PM10</div>
                    <div class='sensor-value'>{data['PM10']}</div>
                </div>
                """, unsafe_allow_html=True)

                st.markdown(f"""
                <div class='live-card'>
                    <div class='label'>NO₂</div>
                    <div class='sensor-value'>{data['NO2']}</div>
                </div>
                """, unsafe_allow_html=True)

            with col3:
                st.markdown(f"""
                <div class='live-card'>
                    <div class='label'>Temperature (°C)</div>
                    <div class='sensor-value'>{data['Temperature']}</div>
                </div>
                """, unsafe_allow_html=True)

                st.markdown(f"""
                <div class='live-card'>
                    <div class='label'>Humidity (%)</div>
                    <div class='sensor-value'>{data['Humidity']}</div>
                </div>
                """, unsafe_allow_html=True)

        time.sleep(0.8)

st.write(" ")
st.write("---")
=======
import streamlit as st
import numpy as np
import time

st.set_page_config(layout="wide")

# ------------------------------------------------------------
# 🌿 PREMIUM UI (Glassmorphism + Card Glow + Animation)
# ------------------------------------------------------------
st.markdown("""
<style>

.live-card {
    background: rgba(255, 255, 255, 0.55);
    backdrop-filter: blur(10px);
    padding: 22px;
    border-radius: 18px;
    box-shadow: 0px 4px 20px rgba(0,0,0,0.15);
    transition: 0.25s ease-in-out;
    text-align: center;
}

.live-card:hover {
    transform: scale(1.02);
    box-shadow: 0px 6px 25px rgba(0,0,0,0.20);
}

.sensor-value {
    font-size: 40px;
    font-weight: 900;
    color: #1B5E20;
}

.label {
    font-size: 20px;
    font-weight: 600;
    color: #555;
}

@keyframes fadeIn {
    0% {opacity: 0; transform: translateY(12px);}
    100% {opacity: 1; transform: translateY(0);}
}

</style>
""", unsafe_allow_html=True)


# ------------------------------------------------------------
# 🌿 HEADER
# ------------------------------------------------------------
st.markdown("""
<h1 style='text-align:center; color:#1B5E20; font-weight:900; animation:fadeIn 0.8s;'>
🚀 Live Pollution Sensor Simulation
</h1>
""", unsafe_allow_html=True)

st.write(" ")
st.write("---")
st.write(" ")

# ------------------------------------------------------------
# 🌿 Live Simulation Function
# ------------------------------------------------------------
def generate_sensor_data():
    return {
        "PM2.5": np.random.randint(10, 300),
        "PM10": np.random.randint(20, 400),
        "CO": round(np.random.uniform(0.1, 5.0), 2),
        "NO2": np.random.randint(5, 200),
        "Temperature": round(np.random.uniform(18, 40), 1),
        "Humidity": np.random.randint(20, 90)
    }


# ------------------------------------------------------------
# 🌿 BUTTON TO START SIMULATION
# ------------------------------------------------------------
start = st.button("🔄 Start Live Simulation", type="primary")

placeholder = st.empty()

if start:
    for i in range(30):
        data = generate_sensor_data()

        with placeholder.container():
            # Row layout
            col1, col2, col3 = st.columns(3)

            with col1:
                st.markdown(f"""
                <div class='live-card'>
                    <div class='label'>PM2.5</div>
                    <div class='sensor-value'>{data['PM2.5']}</div>
                </div>
                """, unsafe_allow_html=True)

                st.markdown(f"""
                <div class='live-card'>
                    <div class='label'>CO (ppm)</div>
                    <div class='sensor-value'>{data['CO']}</div>
                </div>
                """, unsafe_allow_html=True)

            with col2:
                st.markdown(f"""
                <div class='live-card'>
                    <div class='label'>PM10</div>
                    <div class='sensor-value'>{data['PM10']}</div>
                </div>
                """, unsafe_allow_html=True)

                st.markdown(f"""
                <div class='live-card'>
                    <div class='label'>NO₂</div>
                    <div class='sensor-value'>{data['NO2']}</div>
                </div>
                """, unsafe_allow_html=True)

            with col3:
                st.markdown(f"""
                <div class='live-card'>
                    <div class='label'>Temperature (°C)</div>
                    <div class='sensor-value'>{data['Temperature']}</div>
                </div>
                """, unsafe_allow_html=True)

                st.markdown(f"""
                <div class='live-card'>
                    <div class='label'>Humidity (%)</div>
                    <div class='sensor-value'>{data['Humidity']}</div>
                </div>
                """, unsafe_allow_html=True)

        time.sleep(0.8)

st.write(" ")
st.write("---")
>>>>>>> dcaf2231992952bf1ed21ab181fc1543d04f3185
