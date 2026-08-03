import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from resume_analyzer import analyze_resumes

# -----------------------------
# Design Tokens
# -----------------------------

CHART_BG = "#FFFFFF"
INK = "#2B2420"          # warm near-black for text/labels
ACCENT = "#8C3B2E"        # brick/rust - primary accent
ACCENT_2 = "#3E6259"      # deep sage - secondary accent
ACCENT_3 = "#C08B2C"      # ochre/gold - tertiary accent


def style_chart(fig, ax):
    fig.patch.set_facecolor(CHART_BG)
    ax.set_facecolor(CHART_BG)
    ax.tick_params(colors=INK, labelsize=9)
    ax.xaxis.label.set_color(INK)
    ax.yaxis.label.set_color(INK)
    ax.title.set_color(INK)
    ax.title.set_fontweight("bold")
    ax.title.set_fontsize(13)
    ax.grid(axis="y", color="#EDE7DD", linewidth=0.9, zorder=0)
    ax.set_axisbelow(True)
    for side in ["top", "right"]:
        ax.spines[side].set_visible(False)
    for side in ["left", "bottom"]:
        ax.spines[side].set_color("#D9D0C1")

# -----------------------------
# Page Configuration
# -----------------------------

st.set_page_config(
    page_title="AI Resume Screening System",
    page_icon="📄",
    layout="wide"
)

# -----------------------------
# Custom Styling
# -----------------------------

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Fraunces:wght@600;700;800&family=Inter:wght@400;500;600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

/* Main canvas - light background */
.stApp {
    background-color: #FAF7F2;
}

.block-container {
    padding-top: 2.2rem;
    max-width: 1150px;
}

/* Sidebar - animated dark gradient background */
section[data-testid="stSidebar"] {
    background: linear-gradient(-45deg, #2B1B2E, #3E1F2E, #1B2E3A, #16302B);
    background-size: 400% 400%;
    animation: sidebarGradient 15s ease infinite;
    border-right: 1px solid rgba(255,255,255,0.05);
}

@keyframes sidebarGradient {
    0% {
        background-position: 0% 50%;
    }
    50% {
        background-position: 100% 50%;
    }
    100% {
        background-position: 0% 50%;
    }
}

section[data-testid="stSidebar"] * {
    color: #E9E3D8 !important;
}

section[data-testid="stSidebar"] h2 {
    font-family: 'Fraunces', serif;
    color: #FFFFFF !important;
    font-size: 1.2rem;
    font-weight: 700;
    letter-spacing: 0.01em;
    padding-bottom: 0.7rem;
    margin-bottom: 1.1rem;
    position: relative;
}

section[data-testid="stSidebar"] h2::after {
    content: "";
    position: absolute;
    bottom: 0;
    left: 0;
    width: 36px;
    height: 3px;
    background: #C08B2C;
    border-radius: 2px;
}

section[data-testid="stSidebar"] label {
    color: #FFFFFF !important;
    font-weight: 500;
    font-size: 0.88rem;
    text-transform: uppercase;
    letter-spacing: 0.05em;
}

section[data-testid="stSidebar"] .stMultiSelect div[data-baseweb="select"] > div,
section[data-testid="stSidebar"] div[data-testid="stFileUploader"] {
    background: rgba(33, 29, 26, 0.55);
    border-radius: 8px;
    border: 1px solid rgba(255,255,255,0.18);
}

section[data-testid="stSidebar"] span[data-baseweb="tag"] {
    background: #8C3B2E !important;
}

section[data-testid="stSidebar"] .stSlider [role="slider"] {
    background-color: #FFFFFF !important;
    border-color: #FFFFFF !important;
}

/* Sidebar caption / helper text */
section[data-testid="stSidebar"] .stCaption, 
section[data-testid="stSidebar"] small {
    color: #F5F0E8 !important;
}

/* Titles - serif display face for personality */
h1 {
    font-family: 'Fraunces', serif;
    color: #211D1A !important;
    font-weight: 800 !important;
    letter-spacing: -0.01em;
    font-size: 2.4rem !important;
}

h2, h3 {
    font-family: 'Fraunces', serif;
    color: #211D1A !important;
    font-weight: 700 !important;
}

h3 {
    font-size: 1.15rem !important;
    margin-top: 0.4rem !important;
}

/* Intro paragraph under title */
div.block-container > div > div > div > div > p {
    color: #4A423A;
    font-size: 1.02rem;
}

/* Caption under title */
.stApp .stCaption, .stApp small {
    color: #8C3B2E !important;
}

/* Section eyebrow style for subheaders - adds structure/rhythm */
.stApp h3::before {
    content: "";
}

/* Metric cards */
div[data-testid="stMetric"] {
    background: #FFFFFF;
    border: 1px solid #EAE3D6;
    border-top: 3px solid #8C3B2E;
    border-radius: 12px;
    padding: 18px 20px;
    box-shadow: 0 2px 10px rgba(43,36,32,0.05);
}

div[data-testid="stMetricLabel"] {
    color: #8A7F6E !important;
    font-weight: 600 !important;
    font-size: 0.78rem !important;
    text-transform: uppercase;
    letter-spacing: 0.06em;
}

div[data-testid="stMetricValue"] {
    color: #211D1A !important;
    font-family: 'Fraunces', serif;
    font-weight: 700 !important;
}

/* Buttons */
.stButton > button {
    background: #211D1A;
    color: #FBF7F0;
    font-weight: 600;
    border: none;
    border-radius: 8px;
    padding: 0.6em 1.7em;
    transition: background 0.15s ease, transform 0.1s ease;
    letter-spacing: 0.01em;
}

.stButton > button:hover {
    background: #8C3B2E;
    color: #FFFFFF;
    transform: translateY(-1px);
}

/* Download button */
.stDownloadButton > button {
    background: #3E6259;
    color: white;
    font-weight: 600;
    border: none;
    border-radius: 8px;
}

.stDownloadButton > button:hover {
    background: #2F4C44;
}

/* File uploader (main area) */
div[data-testid="stFileUploader"] section {
    background: #FFFFFF;
    border: 1.5px dashed #D9CDBB;
    border-radius: 12px;
}

/* Dataframes */
div[data-testid="stDataFrame"] {
    border: 1px solid #EAE3D6;
    border-radius: 12px;
    overflow: hidden;
}

/* Success / info boxes */
div[data-testid="stAlert"] {
    border-radius: 10px;
    border: 1px solid #EAE3D6;
}

/* Text input */
.stTextInput > div > div > input {
    background: #FFFFFF;
    border: 1px solid #D9CDBB;
    border-radius: 8px;
}

hr {
    border: none !important;
    border-top: 1px solid #EAE3D6 !important;
    margin: 2rem 0 !important;
}

</style>
""", unsafe_allow_html=True)

st.title("📄 AI Resume Screening System")
st.caption("SIGNAL OVER NOISE — SCREEN CANDIDATES BY SKILL FIT, NOT GUESSWORK")
st.write("Upload a CSV file containing candidate resumes and rank them based on skills and experience.")

# -----------------------------
# Upload CSV
# -----------------------------

uploaded_file = st.file_uploader(
    "Upload Resume CSV",
    type=["csv"]
)

# -----------------------------
# Sidebar
# -----------------------------

st.sidebar.header("Screening Settings")
st.sidebar.caption("Tune the criteria used to rank and shortlist candidates.")

available_skills = [
    "Python",
    "SQL",
    "Excel",
    "Power BI",
    "Machine Learning",
    "Java"
]

required_skills = st.sidebar.multiselect(
    "Select Required Skills",
    available_skills,
    default=["Python", "SQL", "Power BI"]
)

min_experience = st.sidebar.slider(
    "Minimum Experience (Years)",
    0,
    10,
    2
)

# -----------------------------
# Analyze
# -----------------------------

if uploaded_file is not None:

    df = pd.read_csv(uploaded_file)

    st.subheader("Uploaded Candidates")

    st.dataframe(df)

    if st.button("Analyze Resumes"):

        ranked_df, shortlisted_df, best = analyze_resumes(
            df,
            required_skills,
            min_experience
        )

        st.success("Resume Analysis Completed!")

        # -----------------------------
        # Best Candidate
        # -----------------------------

        st.subheader("🏆 Best Candidate")

        col1, col2, col3 = st.columns(3)

        col1.metric("Name", best["Name"])
        col2.metric("Resume Score", best["Resume Score"])
        col3.metric("Experience", best["Experience"])

        st.write("---")

        # -----------------------------
        # Statistics
        # -----------------------------

        st.subheader("📊 Statistics")

        c1, c2, c3 = st.columns(3)

        c1.metric(
            "Average Score",
            round(ranked_df["Resume Score"].mean(), 2)
        )

        c2.metric(
            "Highest Score",
            ranked_df["Resume Score"].max()
        )

        c3.metric(
            "Lowest Score",
            ranked_df["Resume Score"].min()
        )

        st.write("---")

        # -----------------------------
        # Ranked Candidates
        # -----------------------------

        st.subheader("📋 Ranked Candidates")

        st.dataframe(ranked_df)

        # -----------------------------
        # Search Candidate
        # -----------------------------

        st.subheader("🔍 Search Candidate")

        search = st.text_input("Enter Candidate Name")

        if search:

            result = ranked_df[
                ranked_df["Name"]
                .str.contains(search, case=False)
            ]

            st.dataframe(result)

        st.write("---")

        # -----------------------------
        # Shortlisted Candidates
        # -----------------------------

        st.subheader("✅ Shortlisted Candidates")

        st.dataframe(shortlisted_df)

        st.write("---")

        # -----------------------------
        # Charts
        # -----------------------------

        st.subheader("📈 Resume Scores")

        fig, ax = plt.subplots(figsize=(10,5))

        ax.bar(
            ranked_df["Name"],
            ranked_df["Resume Score"],
            color=ACCENT,
            edgecolor="none",
            zorder=3
        )

        ax.set_xlabel("Candidates")
        ax.set_ylabel("Score")
        ax.set_title("Resume Score Comparison")

        style_chart(fig, ax)
        plt.xticks(rotation=45)

        st.pyplot(fig)

        # -----------------------------
        # Experience Chart
        # -----------------------------

        st.subheader("📈 Experience")

        fig2, ax2 = plt.subplots(figsize=(10,5))

        ax2.bar(
            ranked_df["Name"],
            ranked_df["Experience"],
            color=ACCENT_2,
            edgecolor="none",
            zorder=3
        )

        ax2.set_xlabel("Candidates")
        ax2.set_ylabel("Years")
        ax2.set_title("Experience Comparison")

        style_chart(fig2, ax2)
        plt.xticks(rotation=45)

        st.pyplot(fig2)

        # -----------------------------
        # Matching Skills Chart
        # -----------------------------

        st.subheader("📈 Matching Skills")

        fig3, ax3 = plt.subplots(figsize=(10,5))

        ax3.bar(
            ranked_df["Name"],
            ranked_df["Matching Skills"],
            color=ACCENT_3,
            edgecolor="none",
            zorder=3
        )

        ax3.set_xlabel("Candidates")
        ax3.set_ylabel("Matched Skills")
        ax3.set_title("Skill Match Comparison")

        style_chart(fig3, ax3)
        plt.xticks(rotation=45)

        st.pyplot(fig3)

        # -----------------------------
        # Download Report
        # -----------------------------

        csv = ranked_df.to_csv(index=False)

        st.download_button(
            label="⬇ Download Resume Report",
            data=csv,
            file_name="Resume_Report.csv",
            mime="text/csv"
        )

else:

    st.info("Please upload a CSV file to begin.")