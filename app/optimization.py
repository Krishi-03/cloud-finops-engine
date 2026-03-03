def optimization_recommendations(df):
    recs = []

    if df['cpu_utilization'].mean() < 30:
        recs.append("Instances are underutilized. Consider downsizing.")

    if (df['instances'] > 0).any() and df['cpu_utilization'].sum() == 0:
        recs.append("Idle resources detected. Remove unused instances.")

    if df['cost'].max() > df['cost'].mean() * 2:
        recs.append("Cost spikes detected. Consider reserved instances.")

    return recs