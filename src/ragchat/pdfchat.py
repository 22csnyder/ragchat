# %% Imports
import os
from pathlib import Path
from typing import List

import streamlit as st
from dotenv import load_dotenv
from langchain.chains.question_answering import load_qa_chain
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.callbacks import get_openai_callback
from langchain_community.embeddings.openai import OpenAIEmbeddings
from langchain_community.llms import OpenAI
from langchain_community.vectorstores import FAISS
from pypdf import PdfReader

# from PyPDF2 import PdfReader



def hello_world():
    return "Hello World"




def create_embeddings_from_reader(reader) -> FAISS:
    """
    Takes a PDF reader object, extracts text, splits it into chunks,
    and creates embeddings using OpenAIEmbeddings.

    Args:
        reader: A PDF reader object with a pages attribute.

    Returns:
        FAISS: A FAISS index object containing the embeddings of the text chunks.
    """
    # Extract text from all pages
    text = "".join([pg.extract_text() for pg in reader.pages])

    # Split into Chunks ("documents")
    text_splitter = CharacterTextSplitter(
        separator="\n|  ",
        is_separator_regex=True,
        chunk_size=2200,
        chunk_overlap=400,
        length_function=len,
    )

    chunks = text_splitter.split_text(text)

    # Create embeddings
    embeddings = OpenAIEmbeddings()
    knowledge_base = FAISS.from_texts(chunks, embeddings)  # "FlatL2")

    return knowledge_base



class App:
    """
    App initializes a streamlit app that enables question-answer format using a text box and a pdf file uploader.
    """
    def __init__(self):
        """
        __init__ initializes app consisting of page with two main components:
                1. pdf: file_uploader to upload pdf file
                2. user_question: text_input to ask question about pdf
            streamlit listens for when either becomes not None after user entry.
            (by default is hosted on localhost:8501)
        """        
        self.style_page()
        # Ask to upload pdf file to extract text from
        self.pdf = st.file_uploader("Upload your PDF", type="pdf")
        # Box for user to input text
        self.user_question = st.text_input("Ask a question about your PDF:")

    @staticmethod
    def set_api_keys():
        """
        load_dotenv sets environment variable OPENAI_API_KEY if defined in .env file
        """        
        load_dotenv()

    def style_page(self):
        st.set_page_config(page_title="Ask your PDF")
        st.header("Ask your PDF 💬")




def main():
    """
     Tools:
         reader = PdfReader(pdf)
         embeddings = OpenAIEmbeddings()
         FAISS   is a     langchain.vectorstores
             docs + question -> vectors
     Logic:
         llm = OpenAI(openai_api_key=openai_api_key)
             tokens as vectors -> response
         chain = load_qa_chain
             docs + question = response
         knowledge_base = FAISS.from_texts(...)
             ... =
             chunks     = CharacterTextSplitter(...)
             embeddings = OpenAIEmbeddings()

     Inputs:
         user_question
         docs = knowledge_base.similarity_search(user_question)
             response = chain.run(input_documents=docs, question=user_question)

    """
    App.set_api_keys()#OPENAI KEY in os.getenv() [.env file]
    app=App()#loads OpenAI API key and initializes page
    chain = load_qa_chain(OpenAI(), chain_type="stuff")
    

    # Ask to upload pdf file to extract text from

    if app.pdf: 


        FYI="PDF Reader Config"+\
        ''' 
            separator regex   : <newline OR <2-spaces>,
            chunk_size        : 2200, #max size of chunk after regex endonuclease
            chunk_overlap     : 400,  #  (measured in characters)
        '''
        reader = PdfReader(app.pdf)# parsing, chunking
        # NOT Perfect. e.g. in-line tables disconnenct text



        # uses FAISS embedding (I think from facebook originally?)
        knowledge_base = create_embeddings_from_reader(reader)

    if app.pdf and app.user_question: #if both defined
        #get relevant chunks
        docs = knowledge_base.similarity_search(app.user_question)
        #I think just vanilla L2 distance

        #langchain and openai magic
        with get_openai_callback() as cb:
            response = chain.run(input_documents=docs, question=app.user_question)
            print(cb)
        
        #display response
        print(response)
        st.write(response)


if __name__ == "__main__":
    main()
