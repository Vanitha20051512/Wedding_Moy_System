import streamlit as st


def payment_page():

    st.title("💳 Payment Page")

    st.subheader("Scan QR Code & Make Payment")


    # Uploaded QR display
    if "qr_path" in st.session_state:

        st.image(
            st.session_state["qr_path"],
            width=300,
            caption="Google Pay / PhonePe QR Code"
        )

    else:
        st.error("Payment QR Code Not Found")


    st.markdown("---")


    st.write("Guest Name:", st.session_state.get("guest_name", ""))
    st.write("Moy Amount:", st.session_state.get("moy_amount", 0))


    if st.button("✅ Payment Completed"):

        st.success("Payment Completed Successfully")


        # Next page (Receipt)
        st.session_state["page"] = "receipt"

        st.rerun()