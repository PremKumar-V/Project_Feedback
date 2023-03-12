from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (
    ForeignKey,
    Column,
    String,
    Integer,
    CHAR,
    Boolean,
    Date,
)

Base = declarative_base()


class Login(Base):
    __tablename__ = "Login"

    id = Column(Integer, primary_key=True)
    profession = Column("profession", String)
    username = Column("username", String)
    password = Column("password", String)

    def __init__(self, profession: str, username: str, password: str):
        self.profession = profession
        self.username = username
        self.password = password

    def __repr__(self) -> str:
        return f"User Login -> Profession: {self.profession}, Username: {self.username}, Password: {self.password}"


class AdminLogin(Base):
    __tablename__ = "AdminLogin"

    id = Column(Integer, primary_key=True)
    username = Column("username", String)
    password = Column("password", String)

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __repr__(self):
        return f"Admin Login -> Username: {self.username}, Password: {self.password}"


class Details(Base):
    __tablename__ = "Details"

    id = Column(Integer, primary_key=True)
    ward = Column("Ward No", String)
    wingno = Column("Wing No", Integer)
    roomno = Column("Room No", Integer)
    pIpno = Column("Patient_IP_No", Integer)
    pName = Column("Patient_Name", String)
    age = Column("Age", Integer)
    sex = Column("Sex", String)
    mstatus = Column("Martial_Status", String)
    address = Column("Address", String)
    phone = Column("Phone No", Integer)
    email = Column("Email", String)
    insurance = Column("Insurance", String)
    category = Column("Category", String)
    admittedon = Column("Admitted_On", Date)
    admittedby = Column("Admitted_By", String)
    dischargedate = Column("Discharge_Date", Date)
    diagnosis = Column("Diagnosis", String)
    consultantName = Column("Consultant Name", String)

    def __init__(
        self,
        ward,
        wingno,
        roomno,
        pIpno,
        pName,
        age,
        sex,
        mstatus,
        address,
        phone,
        email,
        insurance,
        category,
        admittedon,
        admittedby,
        dischargedate,
        diagnosis,
        consultantName,
    ):
        self.ward = ward
        self.wingno = wingno
        self.roomno = roomno
        self.pIpno = pIpno
        self.pName = pName
        self.age = age
        self.sex = sex
        self.sex = sex
        self.mstatus = mstatus
        self.address = address
        self.phone = phone
        self.email = email
        self.insurance = insurance
        self.category = category
        self.admittedon = admittedon
        self.admittedby = admittedby
        self.dischargedate = dischargedate
        self.diagnosis = diagnosis
        self.consultantName = consultantName

    def __repr__(self) -> str:
        return f"{self.ward, self.wingno, self.roomno, self.pIpno,self.pName, self.age, self.sex, self.mstatus,self.address, self.phone, self.email, self.insurance, self.category,self.admittedon, self.admittedby, self.dischargedate, self.diagnosis, self.consultantName}"


class FeedbackForm(Base):
    __tablename__ = "FeedbackForm"

    id = Column(Integer, primary_key=True)
    d_satisfaction = Column("Satisfaction_With_Doctor", Boolean)
    n_satisfaction = Column("Satisfaction_With_Nurse", Boolean)
    medicine_given_time = Column("Medicine Given Timely", Boolean)
    medicalComplains = Column("Medical", String)
    anyOtherComplains = Column("Any Other Complains", String)
    feedbackType = Column("Overall_Feedback_Type", String)
    remarks = Column("Remarks", String)

    def __init__(self, dS, nS, mGT, mC, aOC, fT, remarks) -> None:
        self.d_satisfaction = dS
        self.n_satisfaction = nS
        self.medicine_given_time = mGT
        self.medicalComplains = mC
        self.anyOtherComplains = aOC
        self.feedbackType = fT
        self.remarks = remarks

    def __repr__(self) -> str:
        return f"{self.d_satisfaction, self.n_satisfaction, self.medicine_given_time, self.medicalComplains, self.anyOtherComplains, self.feedbackType, self.remarks}"
