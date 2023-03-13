import streamlit as st
import datetime

from .FeedbackForm import Form
from database.db import session
from database.models import Details


def dateFunc():
    currDate = datetime.datetime.today().strftime("%Y-%m-%d")
    splited = currDate.split("-")
    return datetime.date(int(splited[0]), int(splited[1]), int(splited[2]))


def clearFunc():
    st.session_state["ward"] = "Select"
    st.session_state["wingno"] = "Select"
    st.session_state["roomno"] = "Select"
    st.session_state["patientIpNo"] = ""
    st.session_state["patientName"] = ""
    st.session_state["age"] = 0
    st.session_state["sex"] = "Select"
    st.session_state["mstatus"] = "Select"
    st.session_state["address"] = ""
    st.session_state["pNo"] = ""
    st.session_state["email"] = ""
    st.session_state["insurance"] = "Select"
    st.session_state["category"] = "Select"
    st.session_state["admittedby"] = ""
    st.session_state["admittedon"] = dateFunc()
    st.session_state["dischargedate"] = dateFunc()
    st.session_state["diagnosis"] = ""
    st.session_state["consultantname"] = ""


def search():
    ward = st.session_state["ward"]
    wingno = st.session_state["wingno"]
    room = st.session_state["roomno"]

    pIpno = st.session_state["patientIpNo"]

    if ward and wingno and room:
        result = session.query(Details).filter(
            Details.ward == ward, Details.wingno == wingno, Details.roomno == room
        )
    else:
        result = session.query(Details).filter(Details.pIpno == pIpno)
    arr = []
    for r in result:
        arr.append(r)

    try:
        fillFunc(arr[0])
        st.success("Patient Found")
        # form = Form()
    except IndexError:
        st.error("Patient Not Found")
        clearFunc()


def fillFunc(result):
    st.session_state["ward"] = result.ward
    st.session_state["wingno"] = result.wingno
    st.session_state["roomno"] = result.roomno
    st.session_state["patientIpNo"] = str(result.pIpno)
    st.session_state["patientName"] = result.pName
    st.session_state["age"] = result.age
    st.session_state["sex"] = result.sex
    st.session_state["mstatus"] = result.mstatus
    st.session_state["address"] = result.address
    st.session_state["pNo"] = str(result.phone)
    st.session_state["email"] = result.email
    st.session_state["insurance"] = result.insurance
    st.session_state["category"] = result.category
    st.session_state["admittedby"] = result.admittedby
    st.session_state["admittedon"] = result.admittedon
    st.session_state["dischargedate"] = result.dischargedate
    st.session_state["diagnosis"] = result.diagnosis
    st.session_state["consultantname"] = result.consultantName


class DetailsClass:
    def __init__(self) -> None:
        with st.form("Patiend Details Form"):
            st.title("Patient Details")

            col1, col2, col3 = st.columns(3)
            wardno = col1.selectbox(
                "Ward No", ["Select", "Ward_1", "Ward_2", "Ward_3"], key="ward"
            )
            wingno = col2.selectbox("Wing No",['Select', 1, 2, 3], key="wingno")
            roomno = col3.selectbox("Room No",['Select', 101, 106], key="roomno")
            button = st.form_submit_button("Submit", on_click=search)
            col4, col5 = st.columns(2)
            patientIpNo = col4.text_input("Patiend Ip No", key="patientIpNo")
            patientName = col5.text_input("Patient Name", key="patientName")

            col6, col7, col8 = st.columns(3)
            age = col6.number_input("Age", min_value=0, key="age")
            sex = col7.selectbox(
                "Sex",
                ["Select", "MALE", "FEMALE"],
                key="sex",
            )
            mstatus = col8.selectbox(
                "Martial Status", ["Select", "Married", "Not Married"], key="mstatus"
            )

            address = st.text_area("Address", key="address")

            col9, col10 = st.columns(2)
            phone = col9.text_input("Phone Number", key="pNo")
            email = col10.text_input("Email", key="email")

            col11, col12, col13 = st.columns(3)
            insurance = col11.selectbox(
                "Insurance",
                ["Select", "SIMS", "MMM Health Care", "Mission Medical Care"],
                key="insurance",
            )
            category = col12.selectbox(
                "Category",
                ["Select", "Under Age", "Student Mission", "Aged Care"],
                key="category",
            )
            admittedby = col13.text_input("Admitted By", key="admittedby")

            col14, col15 = st.columns(2)
            admittedon = col14.date_input("Admitted On", key="admittedon")
            dischargedate = col15.date_input("Discharge Date", key="dischargedate")

            col16, col17 = st.columns(2)
            diagnosis = col16.text_input("Diagnosis", key="diagnosis")
            consultantname = col17.text_input("Consultant Name", key="consultantname")

            
