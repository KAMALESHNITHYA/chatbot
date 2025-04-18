import streamlit as st
from chatbot.bot import ChatBot


# Initialize chatbot
chatbot = ChatBot('data/faq.json')

st.set_page_config(page_title="Rajasthan Edu Chatbot", page_icon="🤖")
st.title("🤖 Rajasthan Technical Education Enquiry Chatbot")

st.write("Ask me about admissions, courses, fees, hostels, placements, and more!")

user_input = st.text_input("You: ", "")

if user_input:
    response = chatbot.get_response(user_input)
    st.success(f"🤖: {response}")
