import streamlit as st

# Title
st.title("Streamlit Basics")

# Header
st.header("Main header")

# Subheader
st.subheader("This is a subheader")

# Markdown
st.markdown("This is markdown **text**")
st.markdown("# Header1")
st.markdown("## Header2")
st.markdown("### Header3")

# Caption
st.caption("This is a caption")

# Code block
st.code("""
import pandas as pd
pd.read_csv(my_csv_file)"""
)

# Preformatted text
st.text("Some text")

# LaTeX
st.latex("x = 2^3")

# Divider
st.text("text above the divider")
st.divider()
st.text("text below the divider")

st.write("Some written text")