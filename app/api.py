from fastapi import FastAPI
from pipelines.pipeline import run_pipeline

app = FastAPI()

@app.get("/")
def home():
    return {"message": "LLM Data Quality Engine (Free Local LLM)"}

@app.post("/run-pipeline")
def run():
    report = run_pipeline()
    return report