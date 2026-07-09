import streamlit as st

from backend.chart_generator import chart_generator
from backend.db_agent import db_agent


class DatabasePage:
    """
    Handles the Database Analysis page.
    """

    @staticmethod
    def render():
        """
        Render the Database Analysis page.
        """

        st.title("🗄️ Database Analysis")

        st.write(
            "Ask questions about your business database using natural language."
        )

        question = st.text_area(
            "Enter your question",
            placeholder="Example: Show the top 10 customers by total revenue.",
            height=100,
        )

        if st.button(
            "Analyze",
            type="primary",
            use_container_width=True,
        ):

            if not question.strip():
                st.warning("Please enter a question.")
                return

            with st.spinner("Analyzing your query..."):

                try:

                    result = db_agent.process_query(question)

                    st.success("Analysis completed successfully!")

                    with st.expander("Generated SQL", expanded=False):

                        st.code(
                            result["sql"],
                            language="sql",
                        )

                    st.subheader("Business Insights")

                    st.write(result["summary"])

                    st.subheader("Query Results")

                    st.dataframe(
                        result["data"],
                        use_container_width=True,
                    )

                    figure = chart_generator.generate_chart(
                        result["data"]
                    )

                    if figure is not None:

                        st.subheader("Visualization")

                        st.plotly_chart(
                            figure,
                            use_container_width=True,
                        )

                except Exception as error:

                    st.error(str(error))


database_page = DatabasePage()