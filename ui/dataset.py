import streamlit as st


def show_dataset_health(df):

    rows = df.shape[0]
    columns = df.shape[1]
    missing = df.isnull().sum().sum()
    duplicates = df.duplicated().sum()
    memory = df.memory_usage(deep=True).sum() / (1024 * 1024)

    c1, c2, c3, c4, c5 = st.columns(5)

    c1.metric("Rows", rows)
    c2.metric("Columns", columns)
    c3.metric("Missing", missing)
    c4.metric("Duplicates", duplicates)
    c5.metric("Memory (MB)", f"{memory:.2f}")