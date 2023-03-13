import streamlit as st

from .Viewer import View
from database.db import session
from database.models import AdminLogin

view = View()


def admin_Login_button_func():
    username = st.session_state["Admin_Username"]
    password = st.session_state["Admin_Password"]

    st.session_state["Admin_Username"] = ""
    st.session_state["Admin_Password"] = ""

    userarr = []
    result = session.query(AdminLogin).filter(AdminLogin.username == username)

    for r in result:
        userarr.append(r)

    try:
        if password != userarr[0].password:
            st.error("Invalid Password")
        else:
            st.success("Admin Login Successful")
            # view.run()

    except IndexError:
        st.error("User not found")


class Admin:
    def __init__(self):
        st.title("Admin Login")

        with st.form("Admin Login"):
            adminUsername = st.text_input("Admin Username", key="Admin_Username")
            adminPassword = st.text_input("Admin Password", key="Admin_Password")

            adminbutton = st.form_submit_button(
                "Login", on_click=admin_Login_button_func
            )
