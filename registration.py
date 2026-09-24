
import streamlit as st
import os


# ==========================================
# UPLOAD FOLDER
# ==========================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

UPLOAD_DIR = os.path.join(
    BASE_DIR,
    "uploads"
)

os.makedirs(UPLOAD_DIR, exist_ok=True)


# ==========================================
# REGISTRATION PAGE
# ==========================================

def registration_page():

    st.title("💒 Wedding Moy Registration")


    # ======================================
    # WEBSITE QR CODE + LINK
    # ======================================

    st.subheader("🌐 Wedding Moy Website")

    website_url = (
        "https://weddingmoysystem-outsorzwtyneprswhqtccn.streamlit.app/"
        "?page=registration"
    )

    qr_path = os.path.join(
        BASE_DIR,
        "registration_website_qr.png"
    )


    # QR CODE

    if os.path.exists(qr_path):

        st.image(
            qr_path,
            width=220,
            caption="📱 Scan QR Code to Open Registration"
        )

    else:

        st.error(
            "❌ registration_website_qr.png not found"
        )


    # WEBSITE LINK

    st.markdown("### 🔗 Website Link")

    st.markdown(
        f"[👉 Open Wedding Moy Registration]({website_url})"
    )


    st.markdown("---")


    # ======================================
    # GUEST DETAILS
    # ======================================

    st.subheader("👥 Guest Details")


    guest_name = st.text_input(
        "Guest Name",
        placeholder="Enter Guest Name"
    )


    guest_mobile = st.text_input(
        "Guest Mobile Number",
        placeholder="Enter 10-digit Mobile Number"
    )


    guest_village = st.text_input(
        "Guest Village",
        placeholder="Enter Guest Village"
    )


    moy_amount = st.number_input(
        "Moy Amount",
        min_value=0.0,
        step=100.0
    )


    remarks = st.text_area(
        "Remarks",
        placeholder="Enter remarks if any"
    )


    # ======================================
    # GUEST PHOTO
    # ======================================

    st.subheader("📸 Guest Photo")


    option = st.radio(
        "Photo Source",
        [
            "Gallery Upload",
            "Camera"
        ]
    )


    if option == "Gallery Upload":

        photo = st.file_uploader(
            "Upload Photo",
            type=[
                "jpg",
                "jpeg",
                "png"
            ]
        )

    else:

        photo = st.camera_input(
            "Take Photo"
        )


    st.markdown("---")


    # ======================================
    # CONTINUE TO PAYMENT
    # ======================================

    if st.button(
        "➡️ Continue to Payment",
        use_container_width=True
    ):


        # Guest Name validation

        if guest_name.strip() == "":

            st.error(
                "❌ Enter Guest Name"
            )

            return


        # Guest Mobile validation

        if guest_mobile.strip() == "":

            st.error(
                "❌ Enter Guest Mobile Number"
            )

            return


        if (
            len(guest_mobile.strip()) != 10
            or not guest_mobile.strip().isdigit()
        ):

            st.error(
                "❌ Enter valid 10-digit Mobile Number"
            )

            return


        # Guest Village validation

        if guest_village.strip() == "":

            st.error(
                "❌ Enter Guest Village"
            )

            return


        # Moy Amount validation

        if moy_amount <= 0:

            st.error(
                "❌ Enter Moy Amount"
            )

            return


        # ==================================
        # SAVE PHOTO
        # ==================================

        photo_path = ""


        if photo is not None:

            filename = (
                guest_mobile.strip()
                + ".jpg"
            )


            photo_path = os.path.join(
                UPLOAD_DIR,
                filename
            )


            with open(
                photo_path,
                "wb"
            ) as f:

                f.write(
                    photo.getbuffer()
                )


        # ==================================
        # SAVE GUEST DATA
        # ==================================

        st.session_state["guest_name"] = (
            guest_name.strip()
        )

        st.session_state["guest_mobile"] = (
            guest_mobile.strip()
        )

        st.session_state["guest_village"] = (
            guest_village.strip()
        )

        st.session_state["moy_amount"] = (
            moy_amount
        )

        st.session_state["remarks"] = (
            remarks.strip()
        )

        st.session_state["photo_path"] = (
            photo_path
        )


        # ==================================
        # MOVE TO PAYMENT
        # ==================================

        st.session_state["page"] = "payment"

        st.success(
            "✅ Registration Completed Successfully"
        )

        st.rerun()