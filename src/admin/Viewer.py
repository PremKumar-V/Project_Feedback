import pandas as pd
import streamlit as st
from sqlite3 import connect


def readSql():
    conn = connect("db.db")
    df = pd.read_sql_table("Details", conn)
    return df


class View:
    def __init__(self):
        return

    def run(self):
        st.title("Admin View")
        df = readSql()
        st.dataframe(df)
