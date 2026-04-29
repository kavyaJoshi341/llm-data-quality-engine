def build_prompt(report, context):
    return f"""
    You are a data quality analyst.

    Current Issues:
    {report}

    Similar Past Issues:
    {context}

    Provide:
    - Explanation
    - Causes
    - Fixes
    - Business Impact
    """