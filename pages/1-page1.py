import streamlit as st

st.write(st.session_state["simple_df"])

def update_value():
    st.session_state["page1_textinput"] = st.session_state["_page1_textinput"]

st.text_input("Enter some text", key="_page1_textinput", on_change=update_value)