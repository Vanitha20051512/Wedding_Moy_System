import streamlit as st
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from datetime import datetime
import os

def receipt_page():

    st.title("🧾 Wedding Moy Receipt")

    required = [
        "parent_name",
        "guest_name",
        "guest_mobile",
        "guest_village",
        "moy_amount",
        "receipt_no",
        "payment_status"
    ]

    for item in required:
        if item not in st.session_state:
            st.error("Payment not completed.")
            return

    parent_name = st.session_state["parent_name"]
    guest_name = st.session_state["guest_name"]
    guest_mobile = st.session_state["guest_mobile"]
    guest_village = st.session_state["guest_village"]
    amount = st.session_state["moy_amount"]
    receipt_no = st.session_state["receipt_no"]
    payment_status = st.session_state["payment_status"]
    transaction_id = st.session_state.get("transaction_id", "N/A")

    st.subheader("Receipt Details")

    st.write("Receipt No :", receipt_no)
    st.write("Parent Name :", parent_name)
    st.write("Guest Name :", guest_name)
    st.write("Mobile :", guest_mobile)
    st.write("Village :", guest_village)
    st.write("Amount : ₹", amount)
    st.write("Transaction ID :", transaction_id)
    st.write("Payment Status :", payment_status)
    st.write("Date :", datetime.now().strftime("%d-%m-%Y %H:%M"))

    photo_path = st.session_state.get("photo_path", "")

    if photo_path and os.path.exists(photo_path):
        st.image(photo_path, width=220)

    def generate_pdf():

        os.makedirs("reports", exist_ok=True)

        pdf_name = f"reports/{receipt_no}.pdf"

        doc = SimpleDocTemplate(pdf_name)
        styles = getSampleStyleSheet()

        story = []

        story.append(Paragraph("<b>Wedding Moy Receipt</b>", styles["Title"]))
        story.append(Paragraph(f"Receipt No : {receipt_no}", styles["Normal"]))
        story.append(Paragraph(f"Parent Name : {parent_name}", styles["Normal"]))
        story.append(Paragraph(f"Guest Name : {guest_name}", styles["Normal"]))
        story.append(Paragraph(f"Mobile : {guest_mobile}", styles["Normal"]))
        story.append(Paragraph(f"Village : {guest_village}", styles["Normal"]))
        story.append(Paragraph(f"Amount : ₹ {amount}", styles["Normal"]))
        story.append(Paragraph(f"Transaction ID : {transaction_id}", styles["Normal"]))
        story.append(Paragraph(f"Payment Status : {payment_status}", styles["Normal"]))

        doc.build(story)

        return pdf_name

    if st.button("📄 Generate PDF"):

        pdf = generate_pdf()

        with open(pdf, "rb") as file:
            st.download_button(
                label="📥 Download Receipt",
                data=file,
                file_name=os.path.basename(pdf),
                mime="application/pdf"
            )

    if st.button("🏠 Back To Registration"):

        st.session_state["page"] = "registration"
        st.rerun()