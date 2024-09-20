import streamlit as st


# Title of the app
st.title("Hello coder ravindra dhakad!")

# Text input from the user
name = st.text_input("Enter your name:")

# Display a greeting message
if name:
    st.write(f"Hello, {name}! Welcome to your first Streamlit app.")

# Display a slider
age = st.slider("Select your age", 0, 100, 25)
st.write(f"You selected {age} years old.")

# Display a chart
import numpy as np
import pandas as pd
import altair as alt

# Create a sample dataframe



if st.button('Click me'):
    st.write('Button clicked!')
else:
    st.write('Click the button above.')



st.title("learning platform")

# Create a form for user inputs
with st.form(key="submission_form"):
    name = st.text_input("Enter your name")
    email = st.text_input("Enter your email")
    age = st.number_input("Enter your age", min_value=0, max_value=120)
    
    # Add a submit button
    submit_button = st.form_submit_button(label="Submit")

# Display the submitted data if the form is submitted
if submit_button:
    st.write(f"Name: {name}")
    st.write(f"Email: {email}")
    st.write(f"Age: {age}")

st.title("click and next ")

# Add custom CSS for the red button
st.markdown("""
    <style>
    .red-button {
        background-color: red;
        color: white;
        padding: 10px 20px;
        font-size: 16px;
        border: none;
        border-radius: 5px;
        cursor: pointer;
    }
    .red-button:hover {
        background-color: darkred;
    }
    </style>
    """, unsafe_allow_html=True)

# Create a red button using HTML
if st.markdown('<button class="red-button">Click Me!</button>', unsafe_allow_html=True):
    st.write("Button clicked!")



data = st.selectbox("Enter your lenguge :",("python", "java", "html") )

st.text_input("Enter your name?")

st.text_input("Enter your father name?")

if st.button("like"):
    st.write("like it ")

else:
    st.write("this is good")






st.markdown("this my learnin page and your daily study class data availabal")