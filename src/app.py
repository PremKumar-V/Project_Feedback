import streamlit as st

from admin.Admin import Admin
from Feedback import Login, DetailsForm, FeedbackForm

st.set_page_config(page_title="SRM Feedback")

with st.sidebar:
    choice = st.radio("Pages", ["Feedback Page", "Admin Page"])

if __name__ == "__main__":
    if choice == "Feedback Page":
        login = Login.LoginClass()
        details = DetailsForm.DetailsClass()
        feedbackform = FeedbackForm.Form()
    else:
        admin = Admin()
