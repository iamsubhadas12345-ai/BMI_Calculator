import streamlit as st
from groq import Groq
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Get Groq API key
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    print("GROQ_API_KEY is missing. Please add it to your .env file.")
else:
    print("API_KEY loaded:", GROQ_API_KEY)

# Create Groq client
client = Groq(api_key=GROQ_API_KEY)

st.title("BMI Calculator with AI Nutritionist")

ht = st.slider(
    "Enter your height in meters:",
    min_value=1.0,
    max_value=2.5,
    value=1.7,
    step=0.01
)

wt = st.slider(
    "Enter your weight in kilograms:",
    min_value=1.0,
    max_value=200.0,
    value=70.0,
    step=0.5
)

gender = st.selectbox(
    "Select your gender:",
    ["Male", "Female"]
)

# Calculate BMI
bmi = wt / (ht ** 2)

st.write(f"Your BMI is: {bmi:.2f}")

# Prompt
prompt = f"""
Act like an expert nutritionist.

The user's details are:
- Gender: {gender}
- Height: {ht:.2f} meters
- Weight: {wt:.1f} kg
- BMI: {bmi:.2f}

Comment on the user's BMI and provide general nutrition and lifestyle advice.
Keep the response concise and easy to understand.
"""

# Generate AI response only when button is clicked
if st.button("Analyze your BMI with AI"):
    st.write("Analyzing your BMI with AI...")

    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    st.write(response.choices[0].message.content)

