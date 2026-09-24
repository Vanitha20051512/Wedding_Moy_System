
import streamlit as st
import os


# ==========================================
# LOGIN PAGE
# ==========================================

def login_page():

    st.title("💒 Wedding Moy System")

    st.subheader("🔐 User Login")

    # ======================================
    # USER DETAILS
    # ======================================

    user_name = st.text_input(
        "User Name",
        placeholder="Enter User Name"
    )

    village = st.text_input(
        "Village",
        placeholder="Enter Village"
    )

    mobile = st.text_input(
        "Mobile Number",
        placeholder="Enter 10-digit Mobile Number"
    )

    # ======================================
    # PAYMENT QR CODE UPLOAD
    # ======================================

    st.markdown("---")

    st.subheader("💳 Payment QR Code")

    payment_qr = st.file_uploader(
        "Upload Payment QR Code",
        type=["png", "jpg", "jpeg"],
        help="Upload your Google Pay / PhonePe / UPI QR Code"
    )

    if payment_qr is not None:

        st.image(
            payment_qr,
            width=250,
            caption="Payment QR Code Preview"
        )

    # ======================================
    # LOGIN BUTTON
    # ======================================

    if st.button(
        "🔐 Login",
        use_container_width=True
    ):

        # User name validation
        if user_name.strip() == "":
            st.error("❌ Enter User Name")
            return

        # Village validation
        if village.strip() == "":
            st.error("❌ Enter Village")
            return

        # Mobile validation
        if (
            len(mobile.strip()) != 10
            or not mobile.strip().isdigit()
        ):
            st.error("❌ Enter valid 10-digit Mobile Number")
            return

        # QR validation
        if payment_qr is None:
            st.error("❌ Please upload Payment QR Code")
            return

        # ==================================
        # CREATE UPLOAD FOLDER
        # ==================================

        base_dir = os.path.dirname(
            os.path.abspath(__file__)
        )

        upload_dir = os.path.join(
            base_dir,
            "uploads"
        )

        os.makedirs(
            upload_dir,
            exist_ok=True
        )

        # ==================================
        # SAVE PAYMENT QR
        # ==================================

        qr_path = os.path.join(
            upload_dir,
            "payment_qr.png"
        )

        with open(
            qr_path,
            "wb"
        ) as f:

            f.write(
                payment_qr.getbuffer()
            )

        # ==================================
        # SAVE LOGIN DETAILS
        # ==================================

        st.session_state["login"] = True

        st.session_state["user_name"] = (
            user_name.strip()
        )

        st.session_state["village"] = (
            village.strip()
        )

        st.session_state["mobile"] = (
            mobile.strip()
        )

        st.session_state["qr_path"] = qr_path

        # ==================================
        # GO TO REGISTRATION
        # ==================================

        st.session_state["page"] = "registration"

        st.success(
            "✅ Login Successful"
        )

        st.rerun()