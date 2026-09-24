
import streamlit as st
import os


# ==========================================
# PAYMENT PAGE
# ==========================================

def payment_page():

    st.title("💳 Payment Page")

    st.subheader("📲 Make Payment")

    # ======================================
    # GET PAYMENT QR PATH
    # ======================================

    qr_path = st.session_state.get("qr_path", "")

    # ======================================
    # PAYMENT QR
    # ======================================

    if qr_path and os.path.exists(qr_path):

        st.success("✅ Payment QR Code")

        st.image(
            qr_path,
            width=300,
            caption="Scan using Google Pay / PhonePe / Any UPI App"
        )

    else:

        st.error(
            "❌ Payment QR Code Not Found"
        )

        st.info(
            "Please go back to Login and upload the Payment QR Code."
        )

        if st.button("⬅️ Back to Login"):

            st.session_state["page"] = "login"
            st.session_state["login"] = False

            st.rerun()

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
    # UTR NUMBER
    # ======================================

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

        # Payment status
        st.session_state["payment_status"] = (
            "Pending Verification"
        )

        # Go to receipt
        st.session_state["page"] = "receipt"

        st.success(
            "✅ Payment details submitted successfully!"
        )

        st.rerun()

