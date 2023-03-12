import streamlit as st

from database import models, db


def defineBool(input):
    if input == "Yes":
        return True
    else:
        return False


def clearForm():
    st.session_state["dInput"] = "Yes"
    st.session_state["nInput"] = "Yes"
    st.session_state["mInput"] = "Yes"
    st.session_state["mCInput"] = ""
    st.session_state["aOInput"] = ""
    st.session_state["fInput"] = ""
    st.session_state["rInput"] = ""


def onClick():
    feedbackForm = models.FeedbackForm(
        dS=defineBool(st.session_state["dInput"]),
        nS=defineBool(st.session_state["nInput"]),
        mGT=defineBool(st.session_state["mInput"]),
        mC=st.session_state["mCInput"],
        aOC=st.session_state["aOInput"],
        fT=st.session_state["fInput"],
        remarks=st.session_state["rInput"],
    )
    db.session.add(feedbackForm)
    db.session.commit()
    clearForm()
    st.success("Feedback Saved")


class Form:
    def __init__(self) -> None:
        with st.form("Feedback Form"):
            col1, col2, col3 = st.columns(3)
            dInput = col1.radio("Satisfaction With Doctor", ["Yes", "No"], key="dInput")
            nInput = col2.radio("Satisfaction With Nurse", ["Yes", "No"], key="nInput")
            mInput = col3.radio("Medicine Given Timely", ["Yes", "No"], key="mInput")

            mCInput = st.text_area("Medical Complains", key="mCInput")
            aOInput = st.text_area("Any Other Complains", key="aOInput")

            fInput = st.radio(
                "Overall Feedback Type",
                ["Positive", "Negative", "No Comments"],
                horizontal=True,
                key="fInput",
            )
            rInput = st.text_area("Any Other Remarks", key="rInput")
            st.form_submit_button("Submit", on_click=onClick)
