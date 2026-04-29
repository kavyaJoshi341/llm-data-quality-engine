def check_missing(df):
    return (df.isnull().sum() / len(df) * 100).to_dict()