import streamlit as st
from langchain.schema import HumanMessage, SystemMessage, AIMessage
from langchain_community.chat_models import ChatOpenAI
from dotenv import load_dotenv
import os

# Streamlit UI
st.set_page_config(page_title="Conversational Q&A Chatbot")
st.header("Hey, Let's Chat")

load_dotenv()

chat = ChatOpenAI(openai_api_key=os.getenv("OPEN_API_KEY"),temperature=0.5)

# Initialize session state
if 'flowmessages' not in st.session_state:
    st.session_state['flowmessages'] = [
        SystemMessage(content="You are a comedian AI assistant")
    ]

# Function to load OpenAI model and get response
def get_chatmodel_response(question):
    st.session_state['flowmessages'].append(HumanMessage(content=question))
    answer = chat(st.session_state['flowmessages'])
    st.session_state['flowmessages'].append(AIMessage(content=answer.content))
    return answer.content

user_input = st.text_input("Input: ", key="input")
response = get_chatmodel_response(user_input)

submit = st.button("Ask the question")

# If ask button is clicked
if submit:
    st.subheader("The Response is")
    st.write(response)
