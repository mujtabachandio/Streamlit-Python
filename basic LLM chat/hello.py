import streamlit as st
import requests
import os

# Set Hugging Face API endpoint and token
API_URL = "https://api-inference.huggingface.co/models/facebook/blenderbot-1B-distill"
HEADERS = {"Authorization": f"Bearer {os.getenv('HUGGINGFACE_API_KEY')}"}

def query_huggingface(payload):
    """Function to get response from Hugging Face API"""
    response = requests.post(API_URL, headers=HEADERS, json=payload)
    try:
        return response.json()["generated_text"]
    except (KeyError, TypeError):
        return "Sorry, I couldn't process that."

# Streamlit UI
st.set_page_config(page_title="AI Chatbot", page_icon="💬")
st.title("🤖 AI Chatbot")
st.write("Chat with an AI model using Hugging Face's API!")

# Initialize session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = []
if "user_input" not in st.session_state:
    st.session_state.user_input = ""

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# User input
user_input = st.text_input("Type your message and press Enter:", key="user_input")
if user_input:
    # Display user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.write(user_input)
    
    # Get LLM response
    bot_reply = query_huggingface({"inputs": user_input})
    
    # Display LLM response
    st.session_state.messages.append({"role": "assistant", "content": bot_reply})
    with st.chat_message("assistant"):
        st.write(bot_reply)
    
    # Clear input field by resetting session state
    