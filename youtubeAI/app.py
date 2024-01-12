from dotenv import load_dotenv
import streamlit as streamlit
from langchain.llms import OpenAI

# Load environment variables
load_dotenv()

# App
streamlit.title('YouTube GPT Creator')

prompt = streamlit.text_input('Plug in your prompt here')

#LLMS
llm = OpenAI(model='gpt-3.5-turbo-instruct', temperature=0.9)

#Show to the screen
if prompt:
    response = llm(prompt)
    streamlit.write(response)