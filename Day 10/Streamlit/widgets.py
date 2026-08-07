import streamlit as st
import pandas as pd

st.title("Streamlit Text Input")

name = st.text_input("Enter your name:")

age = st.slider("Select your age:", 0, 100, 25)
st.write(f"Your age is: {age}")

import streamlit as st

options = ["Python", "Java", "C++", "JavaScript"]

choice = st.selectbox("Choose your favorite language:", options)

st.write(f"You selected {choice}.")

if name:
    st.write(f"Hello, {name}")

data = {
    "Name": ["John", "Jane", "Jake", "Jill"],
    "Age": [28, 24, 35, 40],
    "City": ["New York", "Los Angeles", "Chicago", "Houston"]
}

df = pd.DataFrame(data)

# Save DataFrame as a CSV file
df.to_csv("sampledata.csv", index=False)

# Display the DataFrame
st.write(df)

# Upload a CSV file
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

# Read and display the uploaded CSV
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df)