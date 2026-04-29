import streamlit as st
import requests

st.title("LLM Data Quality Engine")

API_URL = "http://127.0.0.1:8000//run-pipeline"

if st.button("Run Data Quality Check"):
    with st.spinner("Running pipeline..."):
        response = requests.post(API_URL)

        if response.status_code == 200:
            report = response.json()

            st.subheader("Missing Values (%)")
            st.write(report["missing"])

            st.subheader("Outliers")
            st.write(report["outliers"])

            st.subheader("Insights")
            st.write(report["insights"])

            st.subheader("LLM Explanation")
            st.write(report["llm_summary"])

        else:
            st.error("Failed to fetch results")