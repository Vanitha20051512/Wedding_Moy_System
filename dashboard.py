
import streamlit as st
import os


def dashboard_page():

    st.title("📊 Wedding Moy Dashboard")

    st.success("🎉 Payment Successful")


    # ======================================
    # GET DATA
    # ======================================

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

    utr_number = st.session_state.get(
        "utr_number",
        ""
    )

    payment_status = st.session_state.get(
        "payment_status",
        "Payment Successful"
    )

    photo_path = st.session_state.get(
        "photo_path",
        ""
    )


    # ======================================
    # SUMMARY
    # ======================================

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(
            "👥 Guest",
            guest_name
        )

    with col2:

        st.metric(
            "💰 Moy Amount",
            f"₹ {amount:.2f}"
        )

    with col3:

        st.metric(
            "💳 Payment",
            "Successful"
        )


    st.markdown("---")


    # ======================================
    # GUEST INFORMATION
    # ======================================

    st.subheader("👥 Guest Information")

    col1, col2 = st.columns(2)

    with col1:

        st.write(
            "👤 **Guest Name:**",
            guest_name
        )

        st.write(
            "📱 **Mobile:**",
            guest_mobile
        )

        st.write(
            "📍 **Village:**",
            guest_village
        )

    with col2:

        st.write(
            "💰 **Moy Amount:**",
            f"₹ {amount:.2f}"
        )

        st.write(
            "🧾 **UTR:**",
            utr_number
        )

        st.write(
            "💳 **Payment Status:**",
            payment_status
        )


    # ======================================
    # GUEST PHOTO
    # ======================================

    st.markdown("---")

    st.subheader("📸 Guest Photo")

    if photo_path and os.path.exists(photo_path):

        st.image(
            photo_path,
            width=300,
            caption=guest_name
        )

    else:

        st.info(
            "📷 Guest photo not uploaded."
        )


    # ======================================
    # REMARKS
    # ======================================

    if remarks:

        st.markdown("---")

        st.subheader("📝 Remarks")

        st.write(remarks)


    # ======================================
    # PAYMENT STATUS
    # ======================================

    st.markdown("---")

    st.success(
        "✅ Payment Successful"
    )
