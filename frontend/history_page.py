import streamlit as st


class HistoryPage:
    """
    Displays query history.
    """

    @staticmethod
    def render():

        st.title("📜 Query History")

        history = st.session_state.get(
            "query_history",
            []
        )

        if not history:

            st.info("No queries have been executed yet.")
            return

        for index, item in enumerate(
            reversed(history),
            start=1
        ):

            with st.expander(f"Query {index}"):

                st.write(
                    f"**Time:** {item['timestamp']}"
                )

                st.write(
                    f"**Question:** {item['question']}"
                )

                st.code(
                    item["sql"],
                    language="sql"
                )

                st.write(item["response"])


history_page = HistoryPage()