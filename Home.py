import streamlit as st

st.set_page_config(
    page_title="AirGuard Dashboard",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ------------------------------------------------------------
# 🎨 PREMIUM UI CSS (Glassmorphism + Animation)
# ------------------------------------------------------------
st.markdown("""
<style>
/* Hide Streamlit default page title */
section[data-testid="stSidebar"] div[data-testid="stSidebarNav"] > div {
    height: 0px !important;
    overflow: hidden !important;
}

/* Sidebar Gradient */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #d2f8d2, #b0f0b0);
    border-right: 2px solid #1B5E20;
    padding-top: 30px !important;
}

/* Main background */
.stApp {
    background: rgba(255, 255, 255, 0.6);
    backdrop-filter: blur(8px);
}

/* Feature Card */
.feature-card {
    background: rgba(255, 255, 255, 0.65);
    padding: 20px;
    border-radius: 18px;
    border: 1px solid #C8E6C9;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.08);
    transition: transform 0.2s ease-in-out;
}

/* Card hover */
.feature-card:hover {
    transform: scale(1.02);
    border: 1px solid #2E7D32;
}

/* Title Animation */
@keyframes fadeSlide {
    0% {opacity: 0; transform: translateY(-10px);}
    100% {opacity: 1; transform: translateY(0px);}
}

h1 {
    animation: fadeSlide 0.8s ease-in-out;
}
</style>
""", unsafe_allow_html=True)

# Fade-in animation
st.markdown("""
<style>
.main, .stApp { animation: fadeIn 0.7s ease-in-out; }
@keyframes fadeIn { 0% {opacity:0;} 100% {opacity:1;} }
</style>
""", unsafe_allow_html=True)

# ------------------------------------------------------------
# 🌿 CUSTOM SIDEBAR
# ------------------------------------------------------------
st.sidebar.markdown("""
<h2 style='color:#1B5E20; font-weight:800; margin-top:-20px;'>
🌿 AirGuard™ Dashboard
</h2>
""", unsafe_allow_html=True)

st.sidebar.write("AI-Powered Pollution Monitoring System")
st.sidebar.write("---")
st.sidebar.info("Use the sidebar navigation to explore features.")

# Header Bar
st.markdown("""
<div style='
    background: linear-gradient(90deg, #1B5E20, #66BB6A);
    padding: 15px;
    border-radius: 10px;
    text-align:center;
    color:white;
    font-size:20px;
    font-weight:700;
    margin-bottom:15px;
'>
🌍 Building a Cleaner Planet with AI
</div>
""", unsafe_allow_html=True)

# ------------------------------------------------------------
# 🌟 MAIN TITLE
# ------------------------------------------------------------
st.markdown("""
<h1 style='text-align:center; font-weight:900; color:#1B5E20;'>
AirGuard™ Premium Pollution Monitoring Dashboard
</h1>
""", unsafe_allow_html=True)

st.markdown("""
<div style='text-align:center; font-size:18px;'>
Welcome to <b>AirGuard™</b> — an AI-powered, eco-friendly pollution analysis dashboard.
</div>
""", unsafe_allow_html=True)

st.write(" ")
st.write("---")

# ------------------------------------------------------------
# 🌟 FEATURE CARDS
# ------------------------------------------------------------
st.markdown("""
<style>
.feature-card {
    background: #ffffff;
    padding: 15px;
    border-radius: 12px;
    box-shadow: 0px 4px 10px rgba(0,0,0,0.1);
    transition: all 0.3s ease;
    border-left: 5px solid #1B5E20;
}
.feature-card:hover {
    transform: translateY(-5px);
    box-shadow: 0px 6px 18px rgba(0,0,0,0.15);
}
.feature-title { font-size:20px; font-weight:700; color:#1B5E20; }
.feature-desc { color:#444; font-size:15px; }
</style>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    st.markdown("""
    <div class="feature-card">
        <h3 class="feature-title">🔄 Live Pollution Simulation</h3>
        <p class="feature-desc">Real-time simulated pollution sensor reading updates.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="feature-card">
        <h3 class="feature-title">📊 AQI Gauge Meter</h3>
        <p class="feature-desc">Beautiful gauge meter showing current AQI level.</p>
    </div>
    """, unsafe_allow_html=True)

col3, col4 = st.columns(2)
with col3:
    st.markdown("""
    <div class="feature-card">
        <h3 class="feature-title">📈 Pollution Trend Graphs</h3>
        <p class="feature-desc">Interactive charts showing daily AQI patterns.</p>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="feature-card">
        <h3 class="feature-title">🤖 AI AQI Prediction</h3>
        <p class="feature-desc">AI model to predict future AQI values.</p>
    </div>
    """, unsafe_allow_html=True)

# ------------------------------------------------------------
# FOOTER
# ------------------------------------------------------------
st.markdown("""
<hr style='border:1px solid #A5D6A7; margin-top:40px;'>

<div style='text-align:center; padding:10px; font-size:18px; color:#1B5E20;'>
<b>AirGuard™</b> — Empowering Cleaner Cities with AI 🌍  
<br>
<span style='font-size:14px; color:#444;'>Team NexGen Yodhas — Medha Manthan Hackathon 1.0</span>
</div>
""", unsafe_allow_html=True)
