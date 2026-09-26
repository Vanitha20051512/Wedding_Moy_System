
import streamlit as st
import os


def receipt_page():

    st.title("🧾 Wedding Moy Receipt")

    st.success("🎉 Payment Successful!")


    # ======================================
    # GUEST DETAILS
    # ======================================

    st.subheader("👥 Guest Details")

    guest_name = st.session_state.get(
        "guest_name",
        ""
    )

    guest_mobile = st.session_state.get(
        "guest_mobile",
        ""
    )

    guest_village = st.session_state.get(
        "guest_village",
        ""
    )

    amount = st.session_state.get(
        "moy_amount",
        0
    )

    remarks = st.session_state.get(
        "remarks",
        ""
    )


    st.write(
        "👤 Guest Name:",
        guest_name
    )

    st.write(
        "📱 Mobile:",
        guest_mobile
    )

    st.write(
        "📍 Village:",
        guest_village
    )

    st.write(
        "💰 Moy Amount:",
        f"₹ {amount:.2f}"
    )

    if remarks:

        st.write(
            "📝 Remarks:",
            remarks
        )


    # ======================================
    # PHOTO
    # ======================================

    photo_path = st.session_state.get(
        "photo_path",
        ""
    )

    if photo_path and os.path.exists(photo_path):

        st.subheader("📸 Guest Photo")

        st.image(
            photo_path,
            width=250
        )


    st.markdown("---")


    # ======================================
    # PAYMENT DETAILS
    # ======================================

    st.subheader("💳 Payment Details")

    utr_number = st.session_state.get(
        "utr_number",
        ""
    )

    payment_status = st.session_state.get(
        "payment_status",
        "Payment Successful"
    )


    st.write(
        "🧾 UTR / Transaction ID:",
        utr_number
    )

    st.success(
        "✅ Payment Status: "
        + payment_status
    )


    st.markdown("---")


    # ======================================
    # DASHBOARD
    # ======================================

    if st.button(
        "📊 Go to Dashboard",
        use_container_width=True
    ):

        st.session_state["page"] = "dashboard"

        st.rerun()