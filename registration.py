import streamlit as st
import os

os.makedirs("uploads", exist_ok=True)


def registration_page():

    if not st.session_state.get("login", False):
        st.session_state["page"] = "login"
        st.rerun()


    st.title("💒 Wedding Moy Registration")

    st.subheader("Parent Details")

    st.text_input(
        "Parent Name",
        value=st.session_state["parent_name"],
        disabled=True
    )

    st.text_input(
        "Village",
        value=st.session_state["village"],
        disabled=True
    )

    st.text_input(
        "Mobile",
        value=st.session_state["mobile"],
        disabled=True
    )


    st.markdown("---")

    st.subheader("Guest Details")

    guest_name = st.text_input("Guest Name")
    guest_mobile = st.text_input("Guest Mobile Number")
    guest_village = st.text_input("Guest Village")

    moy_amount = st.number_input(
        "Moy Amount",
        min_value=0.0,
        step=100.0
    )

    remarks = st.text_area("Remarks")


    st.subheader("Guest Photo")

    option = st.radio(
        "Photo Source",
        ["Gallery Upload", "Camera"]
    )


    if option == "Gallery Upload":
        photo = st.file_uploader(
            "Upload Photo",
            type=["jpg","jpeg","png"]
        )

    else:
        photo = st.camera_input("Take Photo")



    if st.button("Continue to Payment"):


        if guest_name.strip() == "":
            st.error("Enter Guest Name")
            return


        if guest_mobile.strip() == "":
            st.error("Enter Guest Mobile Number")
            return


        if len(guest_mobile) != 10 or not guest_mobile.isdigit():
            st.error("Enter valid 10-digit Mobile Number")
            return


        if guest_village.strip() == "":
            st.error("Enter Guest Village")
            return


        if moy_amount <= 0:
            st.error("Enter Moy Amount")
            return



        photo_path = ""


        if photo is not None:

            filename = guest_mobile + ".jpg"

            photo_path = os.path.join(
                "uploads",
                filename
            )

            with open(photo_path,"wb") as f:
                f.write(photo.getbuffer())



        # Save guest data

        st.session_state["guest_name"] = guest_name
        st.session_state["guest_mobile"] = guest_mobile
        st.session_state["guest_village"] = guest_village
        st.session_state["moy_amount"] = moy_amount
        st.session_state["remarks"] = remarks
        st.session_state["photo_path"] = photo_path


        # Move to Payment page
        st.session_state["page"] = "payment"

        st.success("Registration Completed Successfully")

        st.rerun()