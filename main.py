import numpy as np
import pandas as pd
import requests
import streamlit as st

global data_set

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

st.title("Employee Turnover Analysis using AI and Machine Learning")
st.title("Company Name : Portobello Tech")
st.write("## Developed by : Mr. Lokendra Kumar Agrawal")

# Add some example content
st.write("## This Tools will suggest you !!!!")
st.write("1. various retention strategies for targeted employees.")
st.write("2. categorize the employees into four zones.")
st.write("▪ Safe Zone (Green) (Score < 20%)")
st.write("▪ Low-Risk Zone (Yellow) (20% < Score < 60%)")
st.write("▪ Medium-Risk Zone (Orange) (60% < Score < 90%)")
st.write("▪ High-Risk Zone (Red) (Score > 90%)")

# Add a simple input and output
name = st.text_input("Enter Customer Name  :")
if name:
    st.write(f"Hello , {name}! ")
    st.write(f"Your report will be ready in few minutes")

# image ID
file_id = "1XM3dOmnOsRYJjU5uWP07ixU4G0HTParr"
csv_file_id = "1o_dBdB3qeCh1HlSHcyiw2_uEQYzCclsE"
# URL
image_url = f"https://drive.google.com/uc?export=view&id={file_id}"
csv_url = f"https://drive.google.com/uc?export=view&id={csv_file_id}"

try:
    response = requests.get(image_url)
    data_set = pd.read_csv(csv_url)

    st.image(response.content, caption="Developer Image", width=200)
    st.write(data_set.head())
except Exception as e:
    st.write("Error loading image of data set:", e)

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=["a", "b", "c"]
)
st.line_chart(chart_data)

# Add a button
if st.button("Calculate !"):
    st.write("Check output file!")
    # step 1 Perform data quality checks by checking for missing values, if any.
    st.write("## 1. checking for missing values")
    st.write(data_set.isna().sum())

