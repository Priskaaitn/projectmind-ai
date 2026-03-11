import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# =====================
# PAGE CONFIG
# =====================

st.set_page_config(
    page_title="ProjectMind AI",
    page_icon="🤖",
    layout="wide"
)

# =====================
# LOAD CSS
# =====================

def load_css():
    with open("style/style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()

# =====================
# TITLE
# =====================

st.title("🤖 ProjectMind AI Dashboard")
st.write("Smart Portfolio Monitoring & Risk Insight System")

uploaded_file = st.file_uploader("Upload Project Report (PDF or CSV)", type=["pdf", "csv"])

if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
else:
    data = pd.read_csv("project_reports.csv")

# =====================
# LOAD CSS
# =====================

def load_css():
    with open("style/style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()

# =====================
# SIDEBAR
# =====================

st.sidebar.markdown("## 🤖 ProjectMind AI")

st.sidebar.markdown("---")

page = st.sidebar.radio(
    "📂 Navigation Menu",
    [
        "🏠 Dashboard",
        "📈 Trend Analysis",
        "📊 Project Data",
        "🧠 AI Insights"
    ]
)

st.sidebar.markdown("---")

st.sidebar.info("""
ProjectMind AI  
Smart Project Portfolio Monitoring
""")

# =====================
# DASHBOARD
# =====================

if page == "🏠 Dashboard":

    st.header("Project Overview")

    total = len(data)
    green = len(data[data["status"]=="green"])
    orange = len(data[data["status"]=="orange"])
    red = len(data[data["status"]=="red"])

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Total Projects", total)
    col2.metric("On Track", green)
    col3.metric("Warning", orange)
    col4.metric("At Risk", red)

    st.divider()

    col5, col6 = st.columns(2)

    # STATUS GRAPH
    with col5:

        st.subheader("Project Status Distribution")

        status_count = data["status"].value_counts()

        fig, ax = plt.subplots()

        colors = ["green","orange","red"]

        ax.bar(status_count.index, status_count.values, color=colors[:len(status_count)])

        ax.set_xlabel("Status")
        ax.set_ylabel("Number of Projects")

        st.pyplot(fig)

    # RISK GRAPH
    with col6:
        st.subheader("Top Project Risks")

        risk_count = data["risk"].value_counts()

        fig2, ax2 = plt.subplots(figsize=(8, 5))

    # Tampilkan horizontal bar agar label tidak tumpang tindih
        ax2.barh(risk_count.index, risk_count.values, color="#1f77b4")
        ax2.set_xlabel("Frequency")
        ax2.set_ylabel("Risk Type")

    # Rapikan label
        ax2.tick_params(axis='y', labelsize=9)
        plt.tight_layout()
        st.pyplot(fig2)

# =====================
# TREND ANALYSIS
# =====================
elif page == "📈 Trend Analysis":

    st.header("Project Trend per Month")

    # Hanya 1 dropdown pilih kolom bulan
    month_col = st.selectbox("📅 Pilih Kolom Bulan", data.columns)

    try:
        month_order = ["January","February","March","April","May","June",
                       "July","August","September","October","November","December"]

        trend = data.groupby(month_col)["name"].count().reset_index()
        trend.columns = ["Month", "Total Projects"]

        if trend["Month"].isin(month_order).any():
            trend["Month"] = pd.Categorical(trend["Month"], categories=month_order, ordered=True)
            trend = trend.sort_values("Month")

        fig, ax = plt.subplots(figsize=(10, 5))
        ax.plot(trend["Month"], trend["Total Projects"], marker="o", linewidth=2, color="#1f77b4")
        ax.fill_between(range(len(trend)), trend["Total Projects"], alpha=0.1, color="#1f77b4")
        ax.set_xticks(range(len(trend)))
        ax.set_xticklabels(trend["Month"], rotation=45)
        ax.set_xlabel("Month")
        ax.set_ylabel("Number of Projects")
        ax.set_title("Project Trend per Month")
        plt.tight_layout()
        st.pyplot(fig)

    except Exception as e:
        st.error(f"Gagal membuat grafik: {e}")
# =====================
# PROJECT DATA
# =====================

elif page == "📊 Project Data":

    st.header("Project Database")

    status_filter = st.selectbox(
        "Filter Project Status",
        ["All","green","orange","red"]
    )

    if status_filter != "All":
        filtered = data[data["status"] == status_filter]
    else:
        filtered = data

    st.dataframe(filtered, use_container_width=True)

# =====================
# AI INSIGHTS
# =====================

elif page == "🧠 AI Insights":

    st.header("AI Insights & Lessons Learned")

    lesson_text = " ".join(data["lesson"])

    wordcloud = WordCloud(
        width=900,
        height=400,
        background_color="white"
    ).generate(lesson_text)

    fig, ax = plt.subplots()

    ax.imshow(wordcloud)
    ax.axis("off")

    st.subheader("Lessons Learned Word Cloud")

    st.pyplot(fig)

    st.divider()

    # AI SUMMARY
    status_count = data["status"].value_counts()
    risk_count = data["risk"].value_counts()

    st.subheader("AI Generated Portfolio Insight")

    st.info(f"""
AI analysis result:

• {status_count.get('green',0)} projects are running smoothly

• {status_count.get('orange',0)} projects require attention

• {status_count.get('red',0)} projects are at high risk

Most common project risk:
{risk_count.idxmax()}
""")