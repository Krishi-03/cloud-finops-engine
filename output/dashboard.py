import streamlit as st
import pandas as pd

df = pd.read_csv("data\sample_usage.csv")

st.title("Cloud Cost Dashboard")

st.line_chart(df['cost'])

st.write("Cost Breakdown")
st.bar_chart(df.groupby('service')['cost'].sum())