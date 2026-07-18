import streamlit as st
import sqlite3
import pandas as pd

def dashboard_page():

    st.title("📊 Wedding Moy Dashboard")

    conn = sqlite3.connect("moy.db", check_same_thread=False)

    try:
        df = pd.read_sql_query("SELECT * FROM moy_records", conn)
    except:
        df = pd.DataFrame()

    total_guest = len(df)

    if total_guest > 0:
        total_amount = df["moy_amount"].sum()
    else:
        total_amount = 0

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Total Guests", total_guest)

    with col2:
        st.metric("Total Collection", f"₹ {total_amount}")

    st.divider()

    st.subheader("All Moy Records")

    if len(df) > 0:
        st.dataframe(df, use_container_width=True)
    else:
        st.info("No Records Found")