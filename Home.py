<<<<<<< HEAD
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
/* Hide Streamlit default page title in the sidebar */
section[data-testid="stSidebar"] div[data-testid="stSidebarNav"] > div {
    height: 0px !important;
    overflow: hidden !important;
}

/* Sidebar Premium Gradient */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #d2f8d2, #b0f0b0);
    border-right: 2px solid #1B5E20;
    padding-top: 30px !important;
}

/* Main background Glassmorphism */
.stApp {
    background: rgba(255, 255, 255, 0.6);
    backdrop-filter: blur(8px);
}

/* Card Container */
.feature-card {
    background: rgba(255, 255, 255, 0.65);
    padding: 20px;
    border-radius: 18px;
    border: 1px solid #C8E6C9;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.08);
    transition: transform 0.2s ease-in-out;
}

/* Card Hover */
.feature-card:hover {
    transform: scale(1.02);
    border: 1px solid #2E7D32;
}

/* Title animation */
@keyframes fadeSlide {
  0% {opacity: 0; transform: translateY(-10px);}
  100% {opacity: 1; transform: translateY(0px);}
}

h1 {
    animation: fadeSlide 0.8s ease-in-out;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<style>

/* Full page fade animation */
.main, .stApp {
    animation: fadeIn 0.7s ease-in-out;
}

@keyframes fadeIn {
    0% {opacity: 0;}
    100% {opacity: 1;}
}

</style>
""", unsafe_allow_html=True)

# ------------------------------------------------------------
# 🌿 CUSTOM SIDEBAR TITLE
# ------------------------------------------------------------
st.sidebar.markdown("""
<h2 style='color:#1B5E20; font-weight:800; margin-top:-20px;'>
🌿 AirGuard™ Dashboard
</h2>
""", unsafe_allow_html=True)

st.sidebar.write("AI-Powered Pollution Monitoring System")
st.sidebar.write("---")
st.sidebar.info("Use the navigation on the left to explore the features.")


# Premium gradient top bar
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
🌍 Building a Smarter & Cleaner Planet with AI
</div>
""", unsafe_allow_html=True)



# ------------------------------------------------------------
# 🌟 PREMIUM SIDEBAR ICONS + HOVER ANIMATION
# ------------------------------------------------------------
st.markdown("""
<style>

/* Sidebar Menu Items Styling */
.css-17eq0hr a {
    font-size: 18px !important;
    font-weight: 600 !important;
    padding: 10px 5px;
    border-radius: 10px;
    color: #1B5E20 !important;
    transition: all 0.2s ease-in-out;
}

/* Hover effect for sidebar menu */
.css-17eq0hr a:hover {
    background-color: #A5D6A7 !important;
    transform: translateX(6px);
    color: #004d40 !important;
}

/* Selected menu item */
.css-1vbd788 {
    background-color: #81C784 !important;
    border-radius: 10px !important;
    color: white !important;
}

</style>
""", unsafe_allow_html=True)



# ------------------------------------------------------------
# 🌟 MAIN DASHBOARD TITLE
# ------------------------------------------------------------
st.markdown("""
<h1 style='text-align:center; font-weight:900; color:#1B5E20;'>
AirGuard™ Premium Pollution Monitoring Dashboard
</h1>
""", unsafe_allow_html=True)

st.markdown("""
<div style='text-align:center; font-size:18px;'>
Welcome to <b>AirGuard™</b>, an AI-powered, eco-friendly pollution monitoring 
dashboard developed for <b>Medha Manthan Hackathon 1.0</b>.
</div>
""", unsafe_allow_html=True)

st.write(" ")
st.write("---")

# FEATURES HEADER
st.markdown("<h2 style='color:#1B5E20;'>✨ Features Available in This Dashboard</h2>", unsafe_allow_html=True)
# ------------------------------------------------------------
# 🌟 Premium Feature Cards
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
.feature-title {
    font-size: 20px;
    font-weight: 700;
    color: #1B5E20;
}
.feature-desc {
    color: #444444;
    font-size: 15px;
}
</style>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="feature-card">
        <h3 class="feature-title">🔄 Live Pollution Simulation</h3>
        <p class="feature-desc">Real-time simulated pollution sensor readings with smooth updates.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="feature-card">
        <h3 class="feature-title">📊 AQI Gauge Meter</h3>
        <p class="feature-desc">Beautiful gauge meter showing live Air Quality Index level.</p>
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
        <p class="feature-desc">AI-powered prediction of future pollution levels.</p>
    </div>
    """, unsafe_allow_html=True)



# ------------------------------------------------------------
# Footer
# ------------------------------------------------------------
st.markdown("""
<hr style='border: 1px solid #A5D6A7; margin-top:40px;'>

<div style='text-align:center; padding:10px; font-size:18px; color:#1B5E20;'>
<b>AirGuard™</b> — Empowering Cleaner Cities with AI 🌍  
<br>
<span style='font-size:14px; color:#4B4B4B;'>Team NexGen Yodhas — Medha Manthan Hackathon 1.0</span>
</div>
=======
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
/* Hide Streamlit default page title in the sidebar */
section[data-testid="stSidebar"] div[data-testid="stSidebarNav"] > div {
    height: 0px !important;
    overflow: hidden !important;
}

/* Sidebar Premium Gradient */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #d2f8d2, #b0f0b0);
    border-right: 2px solid #1B5E20;
    padding-top: 30px !important;
}

/* Main background Glassmorphism */
.stApp {
    background: rgba(255, 255, 255, 0.6);
    backdrop-filter: blur(8px);
}

/* Card Container */
.feature-card {
    background: rgba(255, 255, 255, 0.65);
    padding: 20px;
    border-radius: 18px;
    border: 1px solid #C8E6C9;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.08);
    transition: transform 0.2s ease-in-out;
}

/* Card Hover */
.feature-card:hover {
    transform: scale(1.02);
    border: 1px solid #2E7D32;
}

/* Title animation */
@keyframes fadeSlide {
  0% {opacity: 0; transform: translateY(-10px);}
  100% {opacity: 1; transform: translateY(0px);}
}

h1 {
    animation: fadeSlide 0.8s ease-in-out;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<style>

/* Full page fade animation */
.main, .stApp {
    animation: fadeIn 0.7s ease-in-out;
}

@keyframes fadeIn {
    0% {opacity: 0;}
    100% {opacity: 1;}
}

</style>
""", unsafe_allow_html=True)

# ------------------------------------------------------------
# 🌿 CUSTOM SIDEBAR TITLE
# ------------------------------------------------------------
st.sidebar.markdown("""
<h2 style='color:#1B5E20; font-weight:800; margin-top:-20px;'>
🌿 AirGuard™ Dashboard
</h2>
""", unsafe_allow_html=True)

st.sidebar.write("AI-Powered Pollution Monitoring System")
st.sidebar.write("---")
st.sidebar.info("Use the navigation on the left to explore the features.")


# Premium gradient top bar
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
🌍 Building a Smarter & Cleaner Planet with AI
</div>
""", unsafe_allow_html=True)



# ------------------------------------------------------------
# 🌟 PREMIUM SIDEBAR ICONS + HOVER ANIMATION
# ------------------------------------------------------------
st.markdown("""
<style>

/* Sidebar Menu Items Styling */
.css-17eq0hr a {
    font-size: 18px !important;
    font-weight: 600 !important;
    padding: 10px 5px;
    border-radius: 10px;
    color: #1B5E20 !important;
    transition: all 0.2s ease-in-out;
}

/* Hover effect for sidebar menu */
.css-17eq0hr a:hover {
    background-color: #A5D6A7 !important;
    transform: translateX(6px);
    color: #004d40 !important;
}

/* Selected menu item */
.css-1vbd788 {
    background-color: #81C784 !important;
    border-radius: 10px !important;
    color: white !important;
}

</style>
""", unsafe_allow_html=True)



# ------------------------------------------------------------
# 🌟 MAIN DASHBOARD TITLE
# ------------------------------------------------------------
st.markdown("""
<h1 style='text-align:center; font-weight:900; color:#1B5E20;'>
AirGuard™ Premium Pollution Monitoring Dashboard
</h1>
""", unsafe_allow_html=True)

st.markdown("""
<div style='text-align:center; font-size:18px;'>
Welcome to <b>AirGuard™</b>, an AI-powered, eco-friendly pollution monitoring 
dashboard developed for <b>Medha Manthan Hackathon 1.0</b>.
</div>
""", unsafe_allow_html=True)

st.write(" ")
st.write("---")

# FEATURES HEADER
st.markdown("<h2 style='color:#1B5E20;'>✨ Features Available in This Dashboard</h2>", unsafe_allow_html=True)
# ------------------------------------------------------------
# 🌟 Premium Feature Cards
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
.feature-title {
    font-size: 20px;
    font-weight: 700;
    color: #1B5E20;
}
.feature-desc {
    color: #444444;
    font-size: 15px;
}
</style>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="feature-card">
        <h3 class="feature-title">🔄 Live Pollution Simulation</h3>
        <p class="feature-desc">Real-time simulated pollution sensor readings with smooth updates.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="feature-card">
        <h3 class="feature-title">📊 AQI Gauge Meter</h3>
        <p class="feature-desc">Beautiful gauge meter showing live Air Quality Index level.</p>
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
        <p class="feature-desc">AI-powered prediction of future pollution levels.</p>
    </div>
    """, unsafe_allow_html=True)



# ------------------------------------------------------------
# Footer
# ------------------------------------------------------------
st.markdown("""
<hr style='border: 1px solid #A5D6A7; margin-top:40px;'>

<div style='text-align:center; padding:10px; font-size:18px; color:#1B5E20;'>
<b>AirGuard™</b> — Empowering Cleaner Cities with AI 🌍  
<br>
<span style='font-size:14px; color:#4B4B4B;'>Team NexGen Yodhas — Medha Manthan Hackathon 1.0</span>
</div>
>>>>>>> dcaf2231992952bf1ed21ab181fc1543d04f3185
""", unsafe_allow_html=True)