import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers


def get_response(topic,no_of_words):
    llm=CTransformers(model='models/llama-2-7b-chat.ggmlv3.q8_0.bin',
                      model_type='llama',
                      config={'max_new_tokens':256,
                              'temperature':0.01})
    
    template="""
        Write a blog for a topic {topic}
        within {no_of_words} words.
            """
    
    prompt=PromptTemplate(input_variables=["topic","no_of_words"],
                          template=template)
    response=llm(prompt.format(topic=topic,no_of_words=no_of_words))
    print(response)
    return response
    


st.set_page_config(page_title="Generate Blogs",
                    page_icon='🤖',
                    layout='centered',
                    initial_sidebar_state='collapsed')

st.header("Generate Blogs 🤖")

input_text=st.text_input("Enter the Blog Topic")

cols1,cols2 = st.columns([5,5])

with cols1:
    no_of_words = st.text_input('No of words')

submit = st.button("Generate")

if submit:
    st.write(get_response(input_text,no_of_words))