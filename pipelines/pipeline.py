import json
import os

from src.ingestion.load import load_data
from src.quality.missing_checks import check_missing
from src.quality.outlier_checks import detect_outliers
from src.quality.schema_checks import validate_schema
from src.insights.insight_generator import generate_basic_insights

from src.rag.embedder import get_embedding
from src.rag.retriever import retrieve_similar
from src.rag.vector_store import add_to_index

from src.llm.llm_engine import generate_llm_summary
from src.llm.prompt_templates import build_prompt

def run_pipeline():
    print("STEP 1: Loading data...")
    df = load_data("C:/Users/ADMIN/OneDrive/Documents/PROJECTS/LLM Powered AI Insights Engine/data/raw/nyc_taxi_sample.csv")

    print("STEP 2: Running checks...")
    missing = check_missing(df)
    outliers = detect_outliers(df, "trip_distance")
    schema = validate_schema(df)
    insights = generate_basic_insights(df)

    report = {
        "missing": missing,
        "outliers": outliers,
        "schema_issues": schema,
        "insights": insights
    }

    print("STEP 3: Running RAG...")
    report_text = str(report)
    embedding = get_embedding(report_text)

    add_to_index(embedding, report_text)
    context = retrieve_similar(embedding)

    print("STEP 4: Running LLM...")
    llm_summary = generate_llm_summary(report, context)

    report["llm_summary"] = llm_summary

    print("STEP 5: Writing file...")

    import os
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    output_path = os.path.join(BASE_DIR, "outputs", "report.json")

    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    with open(output_path, "w") as f:
        json.dump(report, f, indent=4)

    print("✅ Pipeline completed!")
    return report