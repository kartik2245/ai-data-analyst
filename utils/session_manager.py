import streamlit as st
from copy import deepcopy
from datetime import datetime

from utils.constants import (
    DEFAULT_GEMINI_MODEL,
    MAX_HISTORY,
)


DEFAULT_SESSION_STATE = {
    "current_page": "CSV Analysis",

    "uploaded_file": None,
    "dataframe": None,
    "clean_dataframe": None,
    "csv_summary": None,

    "database_connected": False,
    "generated_sql": "",
    "sql_result": None,

    "user_query": "",
    "ai_response": "",
    "analysis_result": "",

    "current_chart": None,

    "query_history": [],

    "theme": "Light",
    "llm_model": DEFAULT_GEMINI_MODEL,
}


def initialize_session():
    """
    Initialize all Streamlit session state variables.
    """

    for key, value in DEFAULT_SESSION_STATE.items():
        if key not in st.session_state:
            st.session_state[key] = deepcopy(value)


def get(key, default=None):
    """
    Retrieve a value from session state.
    """

    return st.session_state.get(key, default)


def set(key, value):
    """
    Store a value in session state.
    """

    st.session_state[key] = value


def delete(key):
    """
    Remove a value from session state.
    """

    if key in st.session_state:
        del st.session_state[key]


def reset():
    """
    Reset the complete application session.
    """

    st.session_state.clear()
    initialize_session()


def add_history(question: str, sql: str, response: str):
    """
    Store an executed query in history.
    """

    history = get("query_history", [])

    history.insert(
        0,
        {
            "question": question,
            "sql": sql,
            "response": response,
            "timestamp": str(datetime.now()),
        }
    )

    if len(history) > MAX_HISTORY:
        history = history[:MAX_HISTORY]

    set("query_history", history)


def get_history():
    """
    Return the complete query history.
    """

    return get("query_history", [])


def clear_history():
    """
    Clear all stored query history.
    """

    set("query_history", [])