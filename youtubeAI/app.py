from dotenv import load_dotenv
import streamlit as streamlit
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain
from langchain.memory import ConversationBufferMemory
from langchain.utilities import WikipediaAPIWrapper

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
    input_variables = ['title', 'wikipedia_research'], 
    template='write me a Youtube script based on this TITLE: {title} while leveraging this wikipedia research: {wikipedia_research}')

title_memory = ConversationBufferMemory(input_key='topic', memory_key='chat_history')
script_memory = ConversationBufferMemory(input_key='title', memory_key='chat_history')

# LLMS
llm = OpenAI(model='gpt-3.5-turbo-instruct', temperature=0.9)
title_chain = LLMChain(llm=llm, prompt=title_template, output_key='title', memory=title_memory)
script_chain = LLMChain(llm=llm, prompt=script_template, output_key='script', memory=script_memory)

wiki = WikipediaAPIWrapper()

# Show to the screen
if prompt:
    title = title_chain.run(prompt)
    wiki_research = wiki.run(prompt)
    script = script_chain.run(title=title, wikipedia_research=wiki_research)
    streamlit.write(title)
    streamlit.write(script)
    
    with streamlit.expander('Title History'):
        streamlit.info(title_memory.buffer)
    with streamlit.expander('Script History'):
        streamlit.info(script_memory.buffer)
    with streamlit.expander('Wikipedia Research'):
        streamlit.info(wiki_research)