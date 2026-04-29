from src.llm.local_llm import generate_local_response
from src.llm.prompt_templates import build_prompt

def generate_llm_summary(report, context):
    prompt = build_prompt(report, context)
    return generate_local_response(prompt)