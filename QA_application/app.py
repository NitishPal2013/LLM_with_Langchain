import streamlit as st

from langchain.schema import HumanMessage, SystemMessage, AIMessage
from langchain_openai import ChatOpenAI

## streamlit UI

st.set_page_config(page_title="Get Your Answer!")
st.header("Welcome!, ask me about STEM(Science, Technology, Engineering, Mathematics)!")

from dotenv import load_dotenv

load_dotenv()

import os


chat = ChatOpenAI(temperature=0.5)

if 'messsages' not in st.session_state:
    st.session_state['messsages'] = [
        SystemMessage(content="You are STEM expert. You need to answer the related question to you expertise.")
    ]

# function to load model 

def get_response(question):
    st.session_state['messsages'].append(HumanMessage(content=question))
    answer = chat.invoke(st.session_state['messsages'])
    st.session_state['messsages'].append(AIMessage(content=answer.content))
    return answer.content

user_input = st.text_input("Input: ", key="input")
response = get_response(user_input)

submit = st.button("Send Query!")

if submit:
    st.subheader("Answer: ")
    st.write(response)