from sklearn.linear_model import LinearRegression
import numpy as np

def forecast_cost(df, days=7):
    df = df.reset_index(drop=True)
    X = np.arange(len(df)).reshape(-1,1)
    y = df['cost'].values

    model = LinearRegression()
    model.fit(X, y)

    future_X = np.arange(len(df), len(df)+days).reshape(-1,1)
    forecast = model.predict(future_X)

    return forecast.tolist()