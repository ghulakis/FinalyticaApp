import streamlit as st

st.title("Finalytica: Your Accounting Assistant")
st.sidebar.header("Navigation")
# Using "with" notation
with st.sidebar:
    add_radio = st.radio(
                        "",
                         ( "Dashboard", "Financial Analysis", "Tax Calculations")
                         )
st.write("Welcome to Finalytica, your AI-powered accounting assistant!")
