import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import time
import numpy as np
from sklearn.linear_model import LinearRegression

# Helper Functions
def display_text_elements():
    st.title("Streamlit Basics")
    st.header("Text examples (This is a header)")
    st.subheader("This is a subheader")
    st.markdown("This is markdown **text**")
    st.markdown("# Header1")
    st.markdown("## Header2")
    st.markdown("### Header3")
    st.caption("This is a caption")
    st.code("import pandas as pd\npd.read_csv(my_csv_file)")
    st.text("Some text")
    st.latex("x = 2^3")
    st.text("text above the divider")
    st.divider()
    st.text("text below the divider")
    st.write("Some written text")

def display_data_elements(df, geo_df):
    st.header("Data display elements")
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
    st.markdown("## Map using coordinates in csv")
    st.map(geo_df)

def display_chart_elements(df):
    st.header("Charting elements")
    st.markdown("## Line chart")
    st.line_chart(df, x="year", y=["col1", "col2", "col3"])
    st.markdown("## Area chart")
    st.area_chart(df, x="year", y=["col1", "col2", "col3"])
    st.markdown("## Bar chart")
    st.bar_chart(df, x="year", y=["col1", "col2", "col3"])
    
    # matplotlib chart
    st.markdown("## matplotlib")
    fig, ax = plt.subplots()
    ax.plot(df.year, df.col1)
    ax.set_title("My figure title")
    ax.set_xlabel("x label")
    ax.set_ylabel("y label")
    fig.autofmt_xdate()
    st.pyplot(fig)

def display_input_widgets(df):
    st.header("Input widgets")
    
    st.divider()
    st.subheader("Buttons")
    if st.button(label="Primary", type="primary"):
        st.write("Hello from primary")
    if st.button(label="Secondary", type="secondary"):
        st.write("Hello from secondary")

    st.divider()
    st.subheader("Checkboxes")
    if st.checkbox("Remember me"):
        st.write("I will remember you")
    else:
        st.write("I will forget you")

    st.divider()
    st.subheader("Radio buttons")
    radio = st.radio("choose a column", options=df.columns[1:], index=0)
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
    number_input = st.number_input("Pick a number", min_value=0, max_value=10, value=0)
    st.write(f"You picked {number_input}")

    st.divider()
    st.subheader("Text area")
    text_area = st.text_area("Enter a comment", height=200, placeholder="Write your comment here")
    st.write(text_area)

def display_forms():
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
        if st.form_submit_button("Submit"):
            st.write(f"""
            Appetizer: {appetizer}
            Main course: {main}
            Dessert: {dessert}
            Are you bringing your own wine: {"yes" if wine else "no"}
            {visit_date} {visit_time} {allergies}
            """)

def display_layout_elements(df):
    st.header("Layout elements")

    # Sidebar
    with st.sidebar:
        st.subheader("Sidebar")
        st.write("Text in the sidebar")

    # Columns
    st.subheader("Columns")
    col1, col2, col3 = st.columns(3)
    col1.write("Text in a column")
    slider2 = col2.slider("Choose a number", min_value=0, max_value=10)
    col3.write(slider2)

    st.divider()
    st.subheader("Tabs")
    tab1, tab2 = st.tabs(["Line plot", "Bar plot"])
    with tab1:
        tab1.write("A line plot")
        st.line_chart(df, x="year", y=["col1", "col2", "col3"])
    with tab2:
        tab2.write("A bar plot")
        st.bar_chart(df, x="year", y=["col1", "col2", "col3"])

    st.divider()
    st.subheader("Expander")
    with st.expander("Click to expand"):
        st.write("I am text that you only see when you expand")

    st.divider()
    st.subheader("Container")
    with st.container():
        st.write("This is inside the container")
    st.write("This is outside the container")

def display_caching_demonstration():
    st.header("Caching Demonstration")

    st.button('Test cache')

    st.subheader("st.cache_data")

    @st.cache_data
    def cache_this_function():
        time.sleep(2)
        out = "I'm done running"

        return out

    out = cache_this_function()
    st.write(out) 

    st.subheader("st.cache_resource")

    @st.cache_resource
    def create_simple_linear_regression():
        time.sleep(2)

        x = np.array([1, 2, 3, 4, 5, 6, 7]).reshape(-1, 1)
        y = np.array([1, 2, 3, 4, 5, 6, 7])

        model = LinearRegression().fit(x, y)

        return model
    
    lr = create_simple_linear_regression()
    x_pred = np.array([11]).reshape(-1, 1)
    pred = lr.predict(x_pred) 

    st.write(f"The prediction is: {pred[0]}")

@st.cache_data
def get_sample_data():
    return pd.read_csv("data/sample.csv", dtype="int")

@st.cache_data
def get_location_data():
    return pd.read_csv("data/sample-map.csv")

def display_stateful_app_demo():
    st.header("Stateful apps demo")
    st.write("Here is the session state:")
    st.write(st.session_state)
    st.button("Update state")

    # set using key-value syntax
    if "key" not in st.session_state:
        st.session_state["key"] = "value"

    # set using attribute syntax
    if "attribute" not in st.session_state:
        st.session_state.attribute = "another value"

    # Read value from session state
    st.write(f'Reading with key/value syntax: {st.session_state["key"]}')
    st.write(f'Reading with the attribute syntax: {st.session_state.attribute}')

    # Update values in state
    st.session_state["key"] = "new value"
    st.session_state.attribute = "updated value"

    # Delete items in state
    del st.session_state["key"]
    del st.session_state.attribute

# Main Execution
if __name__ == "__main__":
    # Load data
    df = get_sample_data()
    geo_df = get_location_data()

    # Display elements
    display_text_elements()
    display_data_elements(df, geo_df)
    display_chart_elements(df)
    display_input_widgets(df)
    display_forms()
    display_layout_elements(df)
    display_caching_demonstration()
    display_stateful_app_demo()
