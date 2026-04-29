def generate_basic_insights(df):
    return {
        "avg_fare" : float(df['fare_amount'].mean()),
        "max_distance" : float(df['trip_distance'].max()),
        "total_trips" : int(len(df))
    }