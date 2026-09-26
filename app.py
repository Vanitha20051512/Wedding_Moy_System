
import streamlit as st

from login import login_page
from registration import registration_page
from payment import payment_page
from receipt import receipt_page
from dashboard import dashboard_page


st.set_page_config(
    page_title="Wedding Moy System",
    page_icon="💒",
    layout="wide"
)


# ==========================================
# INITIAL ROUTING
# ==========================================

page_from_url = st.query_params.get("page")


# ==========================================
# QR / REGISTRATION LINK
# ==========================================

if (
    page_from_url == "registration"
    and not st.session_state.get("route_initialized", False)
):

    st.session_state["page"] = "registration"

    st.session_state["qr_mode"] = True

    st.session_state["route_initialized"] = True


# ==========================================
# NORMAL WEBSITE
# ==========================================

elif (
    "page" not in st.session_state
    and not st.session_state.get("route_initialized", False)
):

    st.session_state["page"] = "login"

    st.session_state["qr_mode"] = False

    st.session_state["route_initialized"] = True


# ==========================================
# CURRENT PAGE
# ==========================================

page = st.session_state.get(
    "page",
    "login"
)


# ==========================================
# PAGE NAVIGATION
# ==========================================

if page == "login":

    login_page()


elif page == "registration":

    registration_page()


elif page == "payment":

    payment_page()


elif page == "receipt":

    receipt_page()


elif page == "dashboard":

    dashboard_page()


else:

    st.session_state["page"] = "login"

    st.rerun()
