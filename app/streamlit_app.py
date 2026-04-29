import streamlit as st
import requests
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Data Quality Engine", layout="wide")

st.title("📊 LLM Data Quality & Insights Dashboard")
st.markdown("Analyze dataset quality and generate intelligent insights")

API_URL = "http://127.0.0.1:8000/run-pipeline"  # change after deployment

# Sidebar
st.sidebar.header("Controls")
run_button = st.sidebar.button("🚀 Run Pipeline")

if run_button:
    with st.spinner("Running pipeline... (first run may take ~20s)"):
        try:
            response = requests.post(API_URL)
        except Exception as e:
            st.error(f"Connection error: {e}")
            st.stop()

    if response.status_code != 200:
        st.error("❌ API failed")
        st.stop()

    report = response.json()

    st.success("✅ Pipeline executed successfully!")

    # ---------------- METRICS ----------------
    col1, col2, col3 = st.columns(3)

    col1.metric("Total Trips", report["insights"]["total_trips"])
    col2.metric("Avg Fare", round(report["insights"]["avg_fare"], 2))
    col3.metric("Max Distance", report["insights"]["max_distance"])

    st.divider()

    # ---------------- MISSING VALUES ----------------
    st.subheader("⚠️ Missing Values (%)")

    missing_df = pd.DataFrame(
        list(report["missing"].items()),
        columns=["Column", "Missing %"]
    )

    st.dataframe(missing_df, use_container_width=True)

    # Bar chart
    fig1, ax1 = plt.subplots()
    ax1.barh(missing_df["Column"], missing_df["Missing %"])
    ax1.set_title("Missing Data Distribution")
    st.pyplot(fig1)

    # ---------------- OUTLIERS ----------------
    st.subheader("🚨 Outliers")

    st.metric("Outliers Detected", report["outliers"])

    # ---------------- SAMPLE VISUAL ----------------
    st.subheader("📈 Key Metrics Comparison")

    chart_df = pd.DataFrame({
        "Metric": ["Avg Fare", "Max Distance"],
        "Value": [
            report["insights"]["avg_fare"],
            report["insights"]["max_distance"]
        ]
    })

    fig2, ax2 = plt.subplots()
    ax2.bar(chart_df["Metric"], chart_df["Value"])
    ax2.set_title("Key Metrics")
    st.pyplot(fig2)

    # ---------------- LLM OUTPUT ----------------
    st.subheader("🤖 AI Insights")

    st.info(report["llm_summary"])