import streamlit as st

from database.db import session
from database.models import Login
from .DetailsForm import DetailsClass


def clickFunction():
    profession = st.session_state["profession"]
    username = st.session_state["username"]
    password = st.session_state["password"]

    st.session_state["profession"] = "Select"
    st.session_state["username"] = ""
    st.session_state["password"] = ""

    userarr = []
    result = session.query(Login).filter(Login.username == username)

    for r in result:
        userarr.append(r)

    try:
        if password != userarr[0].password:
            st.error("Invalid Password")
        else:
            st.success("User Login Successful")
    except IndexError:
        st.error("User not found")


class LoginClass:
    def __init__(self) -> None:
        st.title("Login")
        with st.form("Login"):

            profession = st.selectbox(
                "Profession",
                ["Select", "Nursing", "Guest Relation", "Doctor"],
                key="profession",
            )
            username = st.text_input("Username", key="username")
            password = st.text_input("Password", key="password")

            button = st.form_submit_button("Login", on_click=clickFunction)
