import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np

st.set_page_config(layout="wide")

# ------------------------------------------------------------
# 🌿 PREMIUM UI CSS
# ------------------------------------------------------------
st.markdown("""
<style>

.graph-card {
    background: rgba(255, 255, 255, 0.55);
    backdrop-filter: blur(12px);
    padding: 25px;
    border-radius: 16px;
    box-shadow: 0px 4px 20px rgba(0,0,0,0.15);
    transition: 0.25s ease;
    animation: fadeIn 1s ease-in-out;
}

.graph-card:hover {
    transform: scale(1.01);
    box-shadow: 0px 6px 25px rgba(0,0,0,0.25);
}

@keyframes fadeIn {
    0% { opacity:0; transform:translateY(10px); }
    100% { opacity:1; transform:translateY(0px); }
}

/* Section title */
.sec-title {
    font-size: 28px;
    font-weight: 900;
    color: #1B5E20;
    text-align: center;
    animation: fadeIn 0.8s;
}

</style>
""", unsafe_allow_html=True)

# ------------------------------------------------------------
# 🌿 Title
# ------------------------------------------------------------
st.markdown("<h1 class='sec-title'>📊 Pollution Trend Analysis</h1>", unsafe_allow_html=True)
st.write(" ")
st.write("---")

# ------------------------------------------------------------
# Generate synthetic data for graphs
# ------------------------------------------------------------
days = np.arange(1, 31)
pm25 = np.random.randint(30, 200, 30)
pm10 = np.random.randint(40, 300, 30)
co = np.random.uniform(0.2, 5.0, 30)
aqi = np.random.randint(50, 250, 30)

df = pd.DataFrame({
    "Day": days,
    "PM2.5": pm25,
    "PM10": pm10,
    "CO": co,
    "AQI": aqi
})

# ------------------------------------------------------------
# 🌿 ROW 1: AQI LINE GRAPH
# ------------------------------------------------------------
st.markdown("<h3 class='sec-title'>📈 30-Day AQI Trend</h3>", unsafe_allow_html=True)
with st.container():
    st.markdown("<div class='graph-card'>", unsafe_allow_html=True)

    fig1 = px.line(df, x="Day", y="AQI", markers=True, title="AQI Variation Over Time")
    fig1.update_traces(line_color="#1B5E20")
    fig1.update_layout(height=400, title_font_size=20)

    st.plotly_chart(fig1, use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)

st.write(" ")

# ------------------------------------------------------------
# 🌿 ROW 2: Bar Chart of Pollutants
# ------------------------------------------------------------
st.markdown("<h3 class='sec-title'>📊 Pollutant Level Comparison</h3>", unsafe_allow_html=True)
with st.container():
    st.markdown("<div class='graph-card'>", unsafe_allow_html=True)

    df_avg = df[['PM2.5', 'PM10', 'CO']].mean().reset_index()
    df_avg.columns = ['Pollutant', 'Average Level']

    fig2 = px.bar(df_avg, x="Pollutant", y="Average Level",
                  color="Pollutant",
                  color_discrete_sequence=["#1B5E20", "#66BB6A", "#A5D6A7"],
                  title="Average Pollutant Levels")

    fig2.update_layout(height=400, title_font_size=20)

    st.plotly_chart(fig2, use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)

