import numpy as np
import pandas as pd
import requests
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

global data_set

# Define a function to create and display distribution plots
def plot_distribution(data, column, title):
    fig, ax = plt.subplots()
    sns.histplot(data[column], kde=True, ax=ax)
    ax.set_title(title)
    ax.set_xlabel(column)
    ax.set_ylabel('Frequency')
    st.pyplot(fig)


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
except Exception as e:
    st.write("Error loading image of data set:", e)

# Add a simple input and output
name = st.text_input("Enter Customer Name  :")
if name:
    st.write(f"Hello , {name}! ")
    st.write(f"Your report will be ready in few minutes")

# Added a button
if st.button("1. Click here ! for missing values"):
    # step 1 Perform data quality checks by checking for missing values, if any.
    st.write("## 1. Checking for missing values")
    st.write("\n")
    st.write(data_set.isna().sum())

# Added a button
if st.button("2. Click here ! what contributed most to employee"):
    # step 2 Understand what factors contributed most to employee turnover at EDA
    st.write("## 2. Understand what factors contributed most to employee turnover at EDA")
    st.write("\n")
    st.write("## 2.1 correlation heatmap")
    # Extract numerical features for correlation matrix
    numerical_data = data_set.select_dtypes(include=['float64', 'int64'])
    # Calculate the correlation matrix
    correlation_matrix = numerical_data.corr()

    # Draw the heatmap
    plt.figure(figsize=(10, 8))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
    plt.title('Correlation Matrix Heatmap')

    # Show the heatmap in Streamlit
    st.pyplot(plt)

# Added a button
if st.button("Draw the distribution plot of:"):

    st.write("## 2.2 Draw the distribution plot of:")
    # Set up the Streamlit app
    st.title("Employee Data Distribution Plots")

    # Plot Employee Satisfaction
    plot_distribution(data_set, 'satisfaction_level', 'Employee Satisfaction Distribution')

    # Plot Employee Evaluation
    plot_distribution(data_set, 'last_evaluation', 'Employee Evaluation Distribution')

    # Plot Employee Average Monthly Hours
    plot_distribution(data_set, 'average_montly_hours', 'Employee Average Monthly Hours Distribution')
