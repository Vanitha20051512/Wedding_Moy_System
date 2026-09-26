
import streamlit as st
import os


def payment_page():

    st.title("💳 Payment Page")

    st.subheader("📲 Make Payment")

    # Project folder
    base_dir = os.path.dirname(
        os.path.abspath(__file__)
    )

    # ======================================
    # PAYMENT QR
    # ======================================

    qr_path = st.session_state.get(
        "qr_path",
        ""
    )

    # If Login QR is not available,
    # use permanent payment_qr.png

    if not qr_path or not os.path.exists(qr_path):

        permanent_qr = os.path.join(
            base_dir,
            "payment_qr.png"
        )

        if os.path.exists(permanent_qr):
            qr_path = permanent_qr

    # ======================================
    # SHOW QR
    # ======================================

    if qr_path and os.path.exists(qr_path):

        st.success("✅ Payment QR Code")

        st.image(
            qr_path,
            width=300,
            caption="📱 Scan using Google Pay / PhonePe / UPI"
        )

    else:

        st.error("❌ Payment QR Code Not Found")

        st.info(
            "Please upload payment_qr.png "
            "to the project folder."
        )

        return

    # ======================================
    # AMOUNT
    # ======================================

    amount = st.session_state.get(
        "moy_amount",
        0
    )

    st.markdown("---")

    st.subheader("💰 Payment Amount")

    st.metric(
        "Moy Amount",
        f"₹ {amount:.2f}"
    )

    # ======================================
    # UTR
    # ======================================

    st.subheader("🧾 Transaction Details")

    utr_number = st.text_input(
        "UTR / Transaction ID",
        placeholder="Enter UTR / Transaction ID"
    )

    # ======================================
    # PAYMENT COMPLETED
    # ======================================

    if st.button(
        "✅ Payment Completed",
        use_container_width=True
    ):

        if utr_number.strip() == "":

            st.error(
                "❌ Please enter UTR / Transaction ID"
            )

            return

        # Save UTR
        st.session_state["utr_number"] = (
            utr_number.strip()
        )

        # Payment successful
        st.session_state["payment_status"] = (
            "Payment Successful"
        )

        # ==================================
        # GO TO RECEIPT
        # ==================================

        st.session_state["page"] = "receipt"

        st.rerun()
