import streamlit as st

if "last_column" not in st.session_state:
    st.session_state.last_column = None

from utils.data_loader import DataLoadError, load_csv
from utils.schema import get_schema
from utils.agent import run_agent
from utils.code_executor import execute_code
from utils.explainer import explain_result
from utils.visualizer import draw_chart, save_chart
from utils.data_cleaner import clean_data
from utils.insights import generate_insights
from utils.report_generator import generate_report
from io import StringIO

from ui.dataset import show_dataset_health

from utils.memory import (
    initialize_memory,
    add_message,
    get_history,
    clear_history
)

st.set_page_config(
    page_title="AI Data Analyst",
    page_icon="📊",
    layout="wide"
)

st.title("📊 AI Data Analyst")

initialize_memory()

st.write("Upload a CSV file and analyze it using AI.")

uploaded_file = st.file_uploader(
    "Upload CSV",
    type=["csv"]
)

if uploaded_file is not None:

    try:
        df = load_csv(uploaded_file)

    except DataLoadError as e:
        st.error(str(e))

    else:

        show_dataset_health(df)

        st.divider()

        st.subheader("Dataset Preview")
        

        st.dataframe(
            df.head(),
            use_container_width=True
        )

        st.divider()

        st.subheader("Column Information")

        info = df.dtypes.reset_index()
        info.columns = ["Column", "Data Type"]

        st.dataframe(
            info,
            use_container_width=True,
            hide_index=True
        )

        st.divider()

        st.subheader("Missing Values")

        missing_df = df.isnull().sum().reset_index()
        missing_df.columns = ["Column", "Missing Values"]

        st.dataframe(
            missing_df,
            use_container_width=True,
            hide_index=True
        )

        st.divider()

        st.subheader("Summary Statistics")

        st.dataframe(
          df.describe(include="all").round(2),
          use_container_width=True
   )

st.divider()

if st.button("Generate AI Insights"):

    summary = f"""
Rows: {df.shape[0]}
Columns: {df.shape[1]}
Missing Values: {df.isnull().sum().sum()}
Duplicate Rows: {df.duplicated().sum()}

Schema:

{get_schema(df)}

Summary Statistics:

{df.describe(include="all").to_string()}
"""

    with st.spinner("Generating AI Insights..."):

        insights = generate_insights(summary)

    st.subheader("🤖 AI Insights")

    st.write(insights)

    report = generate_report(
        df=df,
        insights=insights
    )

    st.download_button(
        "Download PDF Report",
        data=report,
        file_name="AI_Data_Report.pdf",
        mime="application/pdf"
    )

st.divider()

st.subheader("Ask AI")

st.subheader("Ask AI")

question = st.text_input(
            "Ask anything about your dataset"
        )
if st.button("Generate Answer"):

            if not question.strip():

                st.warning("Please enter a question.")

            else:

                schema = get_schema(df)

                with st.spinner("Thinking..."):

                    agent = run_agent(
                        schema=schema,
                        question=question
                    )

                # ===============================
                # Analysis
                # ===============================

                if agent["task"] == "analysis":

                    code = agent["code"]

                    success, result = execute_code(
                        code,
                        df
                    )

                    if success:

                        explanation = explain_result(
                            question=question,
                            code=code,
                            result=result
                        )

                        st.subheader("Answer")
                        st.write(explanation)
                        report = generate_report(
                            df=df,
                            insights="Generated during analysis.",
                            question=question,
                            answer=explanation
                        )

                        st.download_button(
                            "Download Analysis Report",
                            data=report,
                            file_name="Analysis_Report.pdf",
                            mime="application/pdf"
                        )

                        with st.expander("Generated Python Code"):
                            st.code(
                                code,
                                language="python"
                            )

                        with st.expander("Execution Result"):
                            st.write(result)

                    else:

                        st.error(result)

                # ===============================
                # Charts
                # ===============================

                elif agent["task"] == "chart": # Expected expression

                    figure, error = draw_chart(
                        df,
                        agent
                    )

                    if error:

                        st.error(error)

                    else:

                        st.pyplot(figure)
                        image = save_chart(figure)
                        st.download_button(
                            "⬇ Download Chart",
                            data=image,
                            file_name="chart.png",
                            mime="image/png"
                        )

                        with st.expander("Chart Details"):
                            st.json(agent)


                        

                # ===============================
                # Data Cleaning
                # ===============================

                elif agent["task"] == "clean":

                    df, message = clean_data(
                        df,
                        agent
                    )

                    st.success(message)

                    st.subheader("Cleaned Dataset")

                    st.dataframe(
                        df.head(),
                        use_container_width=True
                    )
                    csv = df.to_csv(index=False)
                    st.download_button(
                     "⬇ Download Cleaned Dataset",
                     data=csv,
                     file_name="cleaned_dataset.csv",
                     mime="text/csv"
                    )

                # ===============================
                # Unknown
                # ===============================

                else:

                    st.error("Unknown task returned by AI Agent.")