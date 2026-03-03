
def preprocess(df):
    df.sort_values("date")
    df['cost'] = df['cost'].astype(float)
    df.fillna(0,inplace=True)
    return df