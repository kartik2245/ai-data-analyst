"""
AI Data Analyst — Application Entry Point

This module serves as the main entry point for the AI Data Analyst application.
It orchestrates the Streamlit UI for uploading datasets and exploring their
basic structure before analysis.
"""

import streamlit as st

from utils.data_loader import DataLoadError, load_csv

# ---------------------------------------------------------------------------
# Page configuration
# ---------------------------------------------------------------------------
st.set_page_config(
    page_title="AI Data Analyst",
    page_icon="📊",
    layout="wide",
)

# ---------------------------------------------------------------------------
# Header & description
# ---------------------------------------------------------------------------
st.title("📊 AI Data Analyst")
st.markdown(
    "Upload a CSV file to explore your dataset — preview rows, inspect column "
    "types, check for missing values, and review summary statistics."
)

# ---------------------------------------------------------------------------
# File upload
# ---------------------------------------------------------------------------
uploaded_file = st.file_uploader(
    label="Upload a CSV file",
    type=["csv"],
    help="Only comma-separated values (.csv) files are supported.",
)

# ---------------------------------------------------------------------------
# Dataset overview (shown after a successful upload)
# ---------------------------------------------------------------------------
if uploaded_file is not None:
    try:
        df = load_csv(uploaded_file)
    except DataLoadError as exc:
        st.error(str(exc))
    else:
        st.success(f"Successfully loaded **{uploaded_file.name}**")

        st.header("Dataset Overview")

        # Preview — first 5 rows
        with st.expander("Preview (first 5 rows)", expanded=True):
            st.dataframe(df.head(), use_container_width=True)

        # Shape
        with st.expander("Dataset Shape"):
            col_rows, col_cols = st.columns(2)
            col_rows.metric("Rows", f"{df.shape[0]:,}")
            col_cols.metric("Columns", f"{df.shape[1]:,}")

        # Column names
        with st.expander("Column Names"):
            st.write(list(df.columns))

        # Data types
        with st.expander("Data Types"):
            dtype_df = df.dtypes.reset_index()
            dtype_df.columns = ["Column", "Data Type"]
            st.dataframe(dtype_df, use_container_width=True, hide_index=True)

        # Missing values per column
        with st.expander("Missing Values"):
            missing_df = df.isnull().sum().reset_index()
            missing_df.columns = ["Column", "Missing Count"]
            st.dataframe(missing_df, use_container_width=True, hide_index=True)

        # Summary statistics
        with st.expander("Summary Statistics"):
            st.dataframe(df.describe(include="all"), use_container_width=True)
