import streamlit as st
import sqlite3
import pandas as pd

st.set_page_config(
    page_title="Admin Panel",
    page_icon="👨‍💼",
    layout="wide"
)

st.title("👨‍💼 Wedding Moy Admin Panel")

conn = sqlite3.connect("moy.db", check_same_thread=False)

df = pd.read_sql_query(
    "SELECT * FROM moy_records",
    conn
)

st.subheader("All Moy Records")

st.dataframe(
    df,
    use_container_width=True
)

st.markdown("---")

st.subheader("Search Guest")

search = st.text_input("Enter Guest Name")

if search:

    result = df[
        df["guest_name"].str.contains(
            search,
            case=False,
            na=False
        )
    ]

    st.dataframe(
        result,
        use_container_width=True
    )
    # ======================================
# Admin.py - Part 2
# ======================================

st.markdown("---")
st.subheader("📊 Statistics")

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

st.markdown("---")

st.subheader("🗑 Delete Record")

record_id = st.number_input(
    "Record ID",
    min_value=1,
    step=1
)

if st.button("Delete Record"):

    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM moy_records WHERE id=?",
        (record_id,)
    )

    conn.commit()

    st.success("Record Deleted Successfully")

    st.rerun()

st.markdown("---")

st.subheader("📥 Export Data")

csv = df.to_csv(index=False).encode("utf-8")

st.download_button(
    label="Download CSV",
    data=csv,
    file_name="Wedding_Moy_Report.csv",
    mime="text/csv"
)

st.markdown("---")

st.success("Admin Panel Loaded Successfully")