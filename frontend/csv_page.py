import pandas as pd
import streamlit as st

from backend.chart_generator import chart_generator
from backend.csv_agent import csv_agent


class CSVPage:
    """
    Handles the CSV Analysis page.
    """

    @staticmethod
    def render():
        """
        Render the CSV Analysis page.
        """

        st.title("📄 CSV Analysis")

        uploaded_file = st.file_uploader(
            "Upload a CSV file",
            type=["csv"]
        )

        if uploaded_file is None:
            st.info("Please upload a CSV file to begin.")
            return

        dataframe = pd.read_csv(uploaded_file)
        st.session_state["dataframe"] = dataframe

        st.subheader("Dataset Preview")
        st.dataframe(
            dataframe.head(),
            use_container_width=True
        )

        question = st.text_area(
            "Ask a question about your dataset",
            placeholder="Example: Which product category has the highest sales?",
            height=100
        )

        if st.button(
            "Analyze CSV",
            type="primary",
            use_container_width=True
        ):

            if not question.strip():
                st.warning("Please enter a question.")
                return

            with st.spinner("Analyzing dataset..."):

                try:

                    summary = csv_agent.analyze(
                        dataframe,
                        question
                    )

                    st.subheader("AI Analysis")
                    st.write(summary)

                    figure = chart_generator.generate_chart(
                        dataframe
                    )

                    if figure is not None:

                        st.subheader("Visualization")

                        st.plotly_chart(
                            figure,
                            use_container_width=True
                        )

                except Exception as error:

                    st.error(str(error))


csv_page = CSVPage()