import streamlit as st

from frontend.sidebar import sidebar
from frontend.csv_page import csv_page
from frontend.database_page import database_page
from frontend.history_page import history_page
from frontend.settings_page import settings_page

from utils.session_manager import initialize_session


st.set_page_config(
    page_title="AI Business Intelligence Platform",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

initialize_session()

selected_page = sidebar.render()

if selected_page == "Database Analysis":
    database_page.render()

elif selected_page == "CSV Analysis":
    csv_page.render()

elif selected_page == "Query History":
    history_page.render()

elif selected_page == "Settings":
    settings_page.render()