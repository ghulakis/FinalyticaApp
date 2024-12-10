import streamlit as st

st.title("Finalytica: Your Accounting Assistant")
st.sidebar.header("Navigation")
st.sidebar.selectbox("Choose a Feature", ["Dashboard", "Financial Analysis", "Tax Calculations"])
st.write("Welcome to Finalytica, your AI-powered accounting assistant!")
