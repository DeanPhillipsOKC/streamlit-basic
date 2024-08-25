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

st.header("Charting elements")

st.markdown("## Line chart")
st.line_chart(df, x="year", y=["col1", "col2", "col3"])

st.markdown("## Area chart")
st.area_chart(df, x="year", y=["col1", "col2", "col3"])

st.markdown("## Bar chart")
st.bar_chart(df, x="year", y=["col1", "col2", "col3"])

st.markdown("## Map using coordinates in csv")
geo_df = pd.read_csv("data/sample-map.csv")
st.map(geo_df)

st.markdown("## matplotlib")

import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.plot(df.year, df.col1)
ax.set_title("My figure title")
ax.set_xlabel("x label")
ax.set_ylabel("y label")
fig.autofmt_xdate() 

st.pyplot(fig)

st.header("Input widgets (part 1)")

st.divider()
st.subheader("Buttons")
primary_btn = st.button(label="Primary", type="primary")
secondary_btn = st.button(label="Secondary", type="secondary")

if primary_btn:
    st.write("Hello from primary")

if secondary_btn:
    st.write("Hello from secondary")

st.divider()
st.subheader("Checkboxes")
checkbox = st.checkbox("Remember me")

if checkbox:
    st.write("I will remember you")
else:
    st.write("I will forget you")

st.divider()
st.subheader("Radio buttons")

radio = st.radio("choose a column", options=df.columns[1:], index=0, horizontal=False)
st.write(radio)

st.divider()
st.subheader("Select box")

select = st.selectbox("Choose a column", options=df.columns[1:], index=0)
st.write(select)

st.divider()
st.subheader("Multiselect")

multiselect = st.multiselect("Choose as many columns as you want", options=df.columns[1:], default=["col1"], max_selections=3)
st.write(multiselect)

st.divider()
st.subheader("Slider")

slider = st.slider("Pick a number", min_value=0, max_value=10, value=0, step=1)
st.write(slider)

st.divider()
st.subheader("Text input")

text_input = st.text_input("What's your name?", placeholder="John Doe")
st.write(f"Your name is {text_input}")

st.divider()
st.subheader("Number input")

number_input = st.number_input("Pick a numbr", min_value=0, max_value=10, value=0)
st.write(f"You picked {number_input}")

st.divider()
st.subheader("Text area")

text_area = st.text_area("Enter a comment", height=200, placeholder="Write your comment here")
st.write(text_area)

st.divider()
st.subheader("Forms")

with st.form("form_key"):
    st.write("What would you like to order?")
    appetizer = st.selectbox("Appetizers", options=["choice1", "choice2", "choice3"])
    main = st.selectbox("Main course", options=["choice1", "choice2", "choice3"])
    dessert = st.selectbox("Dessert", options=["choice1", "choice2", "choice3"])

    wine = st.checkbox("Are you bringing your own wine?")

    visit_date = st.date_input("When are you coming?")
    visit_time = st.time_input("What time are you coming?")
    
    allergies = st.text_area("Any allergies?", placeholder="Leave us a note for allergies")

    submit_btn = st.form_submit_button("Submit")

    if submit_btn:
        st.write(f"""
Appetizer: {appetizer}

Main course: {main}

Dessert: {dessert}

Are you bringing your own wine: {"yes" if wine else "no"}

{visit_date}
{visit_time}

{allergies}
""")