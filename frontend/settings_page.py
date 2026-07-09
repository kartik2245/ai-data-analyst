import streamlit as st


class SettingsPage:
    """
    Application settings.
    """

    @staticmethod
    def render():

        st.title("⚙️ Settings")

        st.write(
            "Application Version: 1.0"
        )

        st.write(
            "Database: Supabase PostgreSQL"
        )

        st.write(
            "AI Model: Gemini 2.5 Flash"
        )

        st.write(
            "Framework: Streamlit"
        )


settings_page = SettingsPage()