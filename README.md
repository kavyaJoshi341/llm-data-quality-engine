# 📊 LLM Data Quality & Insights Engine

## 🚀 Overview
An end-to-end system that detects data quality issues and generates insights using a local LLM.

## 🧠 Features
- Missing value detection
- Outlier detection
- Schema validation
- RAG-based insights
- Local LLM (no API cost)
- FastAPI backend
- Streamlit dashboard

## ▶️ Run Locally

### Start Backend
uvicorn app.api:app --reload

### Start Frontend
streamlit run app/streamlit_app.py

## 🏗️ Architecture
Streamlit → FastAPI → Pipeline → RAG → LLM

## 👩‍💻 Author
Kavya Joshi
