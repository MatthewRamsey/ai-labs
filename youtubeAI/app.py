from dotenv import load_dotenv
import streamlit as streamlit
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain

# Load environment variables
load_dotenv()

# App
streamlit.title('YouTube GPT Creator')

prompt = streamlit.text_input('Plug in your prompt here')

# Prompt Templates
title_template = PromptTemplate(
    input_variables = ['topic'], 
    template='write me a Youtube video title about {topic}')

# Prompt Templates
script_template = PromptTemplate(
    input_variables = ['title'], 
    template='write me a Youtube script based on this TITLE: {title}')

# LLMS
llm = OpenAI(model='gpt-3.5-turbo-instruct', temperature=0.9)
title_chain = LLMChain(llm=llm, prompt=title_template, output_key='title')
script_chain = LLMChain(llm=llm, prompt=script_template, output_key='script')
sequential_chain = SequentialChain(chains=[title_chain, script_chain], input_variables=['topic'], output_variables=['title', 'script'])

# Show to the screen
if prompt:
    response = sequential_chain({'topic':prompt})
    streamlit.write(response['title'])
    streamlit.write(response['script'])