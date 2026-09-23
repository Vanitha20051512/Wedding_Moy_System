import streamlit as st


def login_page():

    st.title("💒 Wedding Moy System")

    st.subheader("🔐 User Login")

    parent_name = st.text_input(
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

    if st.button("Login / Continue"):

        if parent_name.strip() == "":
            st.error("❌ Enter User Name")
            return

        if village.strip() == "":
            st.error("❌ Enter Village")
            return

        if mobile.strip() == "":
            st.error("❌ Enter Mobile Number")
            return

        if len(mobile.strip()) != 10 or not mobile.strip().isdigit():
            st.error("❌ Enter valid 10-digit Mobile Number")
            return

        st.session_state["login"] = True
        st.session_state["parent_name"] = parent_name.strip()
        st.session_state["village"] = village.strip()
        st.session_state["mobile"] = mobile.strip()

        st.session_state["qr_mode"] = False
        st.session_state["page"] = "registration"

        st.rerun()