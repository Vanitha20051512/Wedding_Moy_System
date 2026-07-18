import streamlit as st


def login_page():

    st.title("💒 Wedding Moy System")

    st.subheader("🔐 Parent Login")

    parent_name = st.text_input("Parent Name")
    village = st.text_input("Village")
    mobile = st.text_input("Mobile Number")

    st.subheader("📲 Upload Payment QR Code")

    qr_file = st.file_uploader(
        "Upload Google Pay / PhonePe QR",
        type=["png", "jpg", "jpeg"]
    )

    if st.button("Login / Continue"):

        if parent_name.strip() == "":
            st.error("Enter Parent Name")
            return

        if village.strip() == "":
            st.error("Enter Village")
            return

        if mobile.strip() == "":
            st.error("Enter Mobile Number")
            return

        if qr_file is None:
            st.error("Upload Payment QR")
            return

        with open("uploaded_qr.png", "wb") as f:
            f.write(qr_file.getbuffer())

        # IMPORTANT
        st.session_state["login"] = True

        st.session_state["parent_name"] = parent_name
        st.session_state["village"] = village
        st.session_state["mobile"] = mobile
        st.session_state["qr_path"] = "uploaded_qr.png"

        st.session_state["page"] = "registration"

        st.rerun()