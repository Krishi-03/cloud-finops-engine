import numpy as np

def detect_anomalies(df, threshold=2):
    mean = df['cost'].mean()
    std = df['cost'].std()

    df['z_score'] = (df['cost'] - mean) / std
    df['anomaly'] = np.where(abs(df['z_score']) > threshold, 1, 0)
    return df