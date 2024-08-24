import streamlit as st

# Title
st.title("Streamlit Basics")

# Header
st.header("Text examples (This is a header)")

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

st.header("Data display elements")

import pandas as pd

df = pd.read_csv("data/sample.csv", dtype="int")

st.markdown("## With dataframe")
st.dataframe(df)

st.markdown("## With write")
st.write(df)

st.markdown("## Simple table (not sorting and stuff)")
st.table(df)

st.markdown("## Metrics")
st.metric(label="Population", value=900, delta=20, delta_color="normal")
st.metric(label="Visitors", value=1123, delta=-100, delta_color="normal")
st.metric(label="Expenses", value=500, delta=33, delta_color="inverse")