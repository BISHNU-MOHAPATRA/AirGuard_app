import streamlit as st

st.set_page_config(page_title="About • AirGuard", page_icon="🌿", layout="wide")

# -----------------------------------------------------------
# Premium CSS Styling (Glassmorphism)
# -----------------------------------------------------------
st.markdown("""
<style>

.section-title {
    font-size: 34px;
    font-weight: 900;
    text-align: center;
    color: #1B5E20;
    margin-bottom: 6px;
}

.section-sub {
    text-align: center;
    color: #444;
    margin-bottom: 25px;
    font-size: 15px;
}

.glass-card {
    background: rgba(255,255,255,0.55);
    backdrop-filter: blur(10px);
    padding: 22px;
    border-radius: 16px;
    box-shadow: 0px 6px 25px rgba(0,0,0,0.12);
    border: 1px solid rgba(35,120,54,0.2);
    margin-bottom: 20px;
    transition: transform 0.2s;
}

.glass-card:hover {
    transform: scale(1.01);
}

.team-card {
    background: rgba(255,255,255,0.55);
    padding: 20px;
    border-radius: 16px;
    width: 260px;
    box-shadow: 0 6px 20px rgba(0,0,0,0.10);
    border: 1px solid rgba(35,120,54,0.2);
    text-align: center;
}

.team-name {
    font-size: 18px;
    font-weight: 800;
    color: #1B5E20;
}

.team-role {
    color: #444;
    font-size: 14px;
    margin-bottom: 6px;
}

.avatar {
    width: 80px;
    height: 80px;
    background: linear-gradient(135deg,#1B5E20,#66BB6A);
    border-radius: 50%;
    color: white;
    font-size: 26px;
    font-weight: 900;
    text-align: center;
    line-height: 80px;
    margin-bottom: 12px;
}

.tech-pill {
    display:inline-block;
    background:#eaf7ec;
    border:1px solid #2e7d32;
    padding:6px 14px;
    border-radius:25px;
    color:#1B5E20;
    font-weight:700;
    margin:4px;
}

.footer {
    text-align:center;
    margin-top:40px;
    color:#1B5E20;
    font-weight:600;
}

</style>
""", unsafe_allow_html=True)


# -----------------------------------------------------------
# HEADER
# -----------------------------------------------------------
st.markdown("<div class='section-title'>🌿 AirGuard™️ — Project Overview</div>", unsafe_allow_html=True)
st.markdown("<div class='section-sub'>AI-powered Pollution Monitoring System for Medha Manthan Hackathon 1.0</div>", unsafe_allow_html=True)


# -----------------------------------------------------------
# PROJECT OVERVIEW CARD
# -----------------------------------------------------------
st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
st.markdown("""
### 📘 What is AirGuard™️?

AirGuard™️ is an AI-driven pollution monitoring dashboard designed to help users understand real-time and predicted Air Quality Index (AQI).  
Our aim is to empower communities with *smart, accessible and intelligent pollution insights* using Artificial Intelligence.
""")
st.markdown("</div>", unsafe_allow_html=True)


# -----------------------------------------------------------
# PROBLEM STATEMENT
# -----------------------------------------------------------
st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
st.markdown("""
### ❗ Problem We Solve

Air pollution is a rising challenge affecting millions.  

People often:
- ❌ Cannot understand AQI values  
- ❌ Cannot predict future pollution  
- ❌ Lack real-time insights  

AirGuard solves this by offering:
- Live pollution sensor simulation  
- AQI gauge meter  
- AI-powered prediction  
- Trend visualization  
- Clean & modern UI  
""")
st.markdown("</div>", unsafe_allow_html=True)


# -----------------------------------------------------------
# FEATURES
# -----------------------------------------------------------
st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
st.markdown("""
### ✨ Key Features

- 🔄 *Live Real-Time Pollution Simulation*  
- 📊 *Interactive Graphs & Trend Analyzer*  
- 🎯 *AQI Gauge Meter*  
- 🤖 *AI-Based AQI Prediction*  
- 🎨 *Premium Multi-Page Dashboard UI*  
""")
st.markdown("</div>", unsafe_allow_html=True)


# -----------------------------------------------------------
# TECH STACK
# -----------------------------------------------------------
st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
st.markdown("### 🛠 Tech Stack Used")
st.markdown("""
<div>
<span class='tech-pill'>Python</span>
<span class='tech-pill'>Streamlit</span>
<span class='tech-pill'>Scikit-Learn</span>
<span class='tech-pill'>NumPy</span>
<span class='tech-pill'>Pandas</span>
<span class='tech-pill'>Plotly</span>
<span class='tech-pill'>Joblib</span>
</div>
""", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)


# -----------------------------------------------------------
# TEAM SECTION
# -----------------------------------------------------------
st.markdown("<div class='section-title'>👥 Meet Our Team</div>", unsafe_allow_html=True)

team = [
    {"name": "Sangram Kumar Mohapatra", "role": "Team Leader / ML / Backend / Deployment"},
    {"name": "Bishnu Mohapatra", "role": "Frontend & UI"},
    {"name": "Gayatri Rout", "role": "Data Analyst"},
    {"name": "Swati Prajna Pati", "role": "Documentation & QA"},
    {"name": "Shubham Khandelwal", "role": "Documentation & QA"},
]

cols = st.columns(3)

idx = 0
for i in range(2):
    for col in cols:
        if idx < len(team):
            initials = "".join([p[0] for p in team[idx]["name"].split()][:2])
            col.markdown(f"""
            <div class='team-card'>
                <div class='avatar'>{initials}</div>
                <div class='team-name'>{team[idx]["name"]}</div>
                <div class='team-role'>{team[idx]["role"]}</div>
            </div>
            """, unsafe_allow_html=True)
            idx += 1


# -----------------------------------------------------------
# FUTURE SCOPE
# -----------------------------------------------------------
st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
st.markdown("""
### 🚀 Future Scope

- IoT sensor integration  
- Live pollution data from government API  
- Real-time city maps  
- Mobile version  
- Smart pollution alerts  
""")
st.markdown("</div>", unsafe_allow_html=True)


# -----------------------------------------------------------
# FOOTER
# -----------------------------------------------------------
st.markdown("<div class='footer'>AirGuard™️ — Built with ❤ by Team NexGen Yodhas</div>", unsafe_allow_html=True)
