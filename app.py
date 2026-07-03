import os
import streamlit as st
from dotenv import load_dotenv
from google import genai

# Load API key
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    st.error("Google API Key not found! Please check your .env file.")
    st.stop()

# Gemini Client
client = genai.Client(api_key=api_key)

# Page Title
st.title("🤖 Simple Gemini Chatbot")
st.write("Ask me anything!")

# User Input
user_input = st.text_input("Enter your question:")

# Button
if st.button("Send"):
    if user_input:
        try:
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=user_input
            )
            st.success(response.text)
        except Exception as e:
            st.error(f"Error: {e}")
    else:
        st.warning("Please enter a question.")