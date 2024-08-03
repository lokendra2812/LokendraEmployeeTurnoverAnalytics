import numpy as np
import pandas as pd
import streamlit as st

# Set the page configuration
st.set_page_config(
    page_title="Employee Turnover Analysis using AI and Machine Learning",
    page_icon=":star:",
    layout="wide",  # Other options: "wide", "centered"
    initial_sidebar_state="collapsed",
    # This is to restrict the initial window size (height and width)
    # Although Streamlit doesn't have a direct way to control window size,
    # You can add instructions for users to resize the window manually.
)

st.title("Developed by Mr. Lokendra Kumar Agrawal!")
st.write("Company Name : Portobello Tech")
st.write("Resize your browser window to a smaller size for a better experience.")

# Add some example content
st.write("## Example Content")
st.write("Here is some example content to display in your app.")
st.write("You can add more elements like text, charts, tables, etc.")

# Add a simple input and output
name = st.text_input("Enter your name:")
if name:
    st.write(f"Hello, {name}!")

# Add a button
if st.button("Click me!"):
    st.write("Button clicked!")

# Add an image (optional)
# You can add an image from a URL or a file
st.image("https://via.placeholder.com/150", caption="Example Image")
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=["a", "b", "c"]
)
st.line_chart(chart_data)
