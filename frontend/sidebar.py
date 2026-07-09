import streamlit as st


class Sidebar:
    """
    Handles the application sidebar.
    """

    @staticmethod
    def render() -> str:
        """
        Render the sidebar and return the selected page.
        """

        with st.sidebar:

            st.title("📊 AI Business Intelligence")

            st.markdown("---")

            page = st.radio(
                "Navigation",
                [
                    "Database Analysis",
                    "CSV Analysis",
                    "Query History",
                    "Settings",
                ],
            )

            st.markdown("---")

            st.caption("Version 1.0")

        return page


sidebar = Sidebar()