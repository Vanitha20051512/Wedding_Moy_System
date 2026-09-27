
import streamlit as st
import os
import shutil


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
    # PAYMENT QR MANAGEMENT
    # ======================================

    st.markdown("---")

    st.subheader("💳 Payment QR Codes")

    st.info(
        "You can upload multiple Payment QR Codes."
    )

    # Project folder
    base_dir = os.path.dirname(
        os.path.abspath(__file__)
    )

    qr_folder = os.path.join(
        base_dir,
        "payment_qrs"
    )

    os.makedirs(
        qr_folder,
        exist_ok=True
    )

    # ======================================
    # UPLOAD MULTIPLE QR
    # ======================================

    payment_qrs = st.file_uploader(
        "Upload Payment QR Codes",
        type=[
            "png",
            "jpg",
            "jpeg"
        ],
        accept_multiple_files=True
    )

    # ======================================
    # SHOW UPLOADED QR PREVIEW
    # ======================================

    if payment_qrs:

        st.write(
            f"📱 {len(payment_qrs)} QR Code(s) selected"
        )

        cols = st.columns(
            min(len(payment_qrs), 4)
        )

        for index, qr in enumerate(payment_qrs):

            with cols[index % len(cols)]:

                st.image(
                    qr,
                    width=150,
                    caption=f"QR {index + 1}"
                )

    # ======================================
    # LOGIN
    # ======================================

    if st.button(
        "🔐 Login",
        use_container_width=True
    ):

        # User name
        if user_name.strip() == "":

            st.error(
                "❌ Enter User Name"
            )

            return

        # Village
        if village.strip() == "":

            st.error(
                "❌ Enter Village"
            )

            return

        # Mobile
        if (
            len(mobile.strip()) != 10
            or not mobile.strip().isdigit()
        ):

            st.error(
                "❌ Enter valid 10-digit Mobile Number"
            )

            return

        # ==================================
        # SAVE MULTIPLE QR CODES
        # ==================================

        if payment_qrs:

            # Delete old QR files
            for old_file in os.listdir(qr_folder):

                old_path = os.path.join(
                    qr_folder,
                    old_file
                )

                if os.path.isfile(old_path):

                    os.remove(old_path)

            # Save new QR files
            for index, qr in enumerate(
                payment_qrs,
                start=1
            ):

                extension = os.path.splitext(
                    qr.name
                )[1].lower()

                qr_filename = (
                    f"payment_qr_{index}"
                    f"{extension}"
                )

                qr_path = os.path.join(
                    qr_folder,
                    qr_filename
                )

                with open(
                    qr_path,
                    "wb"
                ) as f:

                    f.write(
                        qr.getbuffer()
                    )

        # ==================================
        # LOGIN SESSION
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

        # ==================================
        # GO TO REGISTRATION
        # ==================================

        st.session_state["page"] = "registration"

        st.success(
            "✅ Login Successful"
        )

        st.rerun()
