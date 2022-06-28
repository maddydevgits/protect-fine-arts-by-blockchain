import app1_register_art
import app2_verify_art

import streamlit as st

PAGES={
    'Register your Art': app1_register_art,
    'Verify your Art': app2_verify_art
}

st.sidebar.title('Dashboard')
selection=st.sidebar.radio('Go to',list(PAGES.keys()))
page=PAGES[selection]
page.app()