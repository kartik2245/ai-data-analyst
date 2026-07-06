import streamlit as st


def initialize_memory():

    if "history" not in st.session_state:
        st.session_state.history = []


def add_message(role, content):

    st.session_state.history.append(
        {
            "role": role,
            "content": content
        }
    )


def get_history(limit=6):

    return st.session_state.history[-limit:]


def clear_history():

    st.session_state.history = []