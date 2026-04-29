def validate_schema(df):
    expected = {
        "passenger_count": "float64",
        "trip_distance": "float64",
        "fare_amount": "float64"
    }
    
    issues = {}
    for col, dtype in expected.items():
        if str(df[col].dtype) != dtype:
            issues[col] = f"Expected {dtype}, got {df[col].dtype}"
    
    return issues