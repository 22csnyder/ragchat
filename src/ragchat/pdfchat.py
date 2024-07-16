# %% Imports
import os
from pathlib import Path

import streamlit as st
from dotenv import load_dotenv

from langchain.chains.question_answering import load_qa_chain
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.callbacks import get_openai_callback
from langchain_community.embeddings.openai import OpenAIEmbeddings
from langchain_community.llms import OpenAI
from langchain_community.vectorstores import FAISS
# from PyPDF2 import PdfReader
from pypdf import PdfReader


def hello_world():
    return "Hello World"


from typing import List

# from langchain.knowledge import FAISS
from langchain_community.vectorstores import FAISS

# from langchain_community.llms import CharacterTextSplitter


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

    def __init__(self):
        """
        __init__ initializes app consisting of page with two main components:
                1. pdf: file_uploader to upload pdf file
                2. user_question: text_input to ask question about pdf
            streamlit listens for when either becomes not None after user entry.
            (by default is hosted on localhost:8501)
        """        
        self.load_dotenv()#OPENAI KEY and/or other user-specific .env configuration
        self.style_page()
        # Ask to upload pdf file to extract text from
        self.pdf = st.file_uploader("Upload your PDF", type="pdf")
        # Box for user to input text
        self.user_question = st.text_input("Ask a question about your PDF:")


    def load_dotenv(self):
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
    load_dotenv()  # sets env variable ['OPENAI_API_KEY']
    st.set_page_config(page_title="Ask your PDF")
    st.header("Ask your PDF 💬")

    # Ask to upload pdf file to extract text from
    pdf = st.file_uploader("Upload your PDF", type="pdf")
    if pdf:
        reader = PdfReader(pdf)
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

        # create embeddings
        embeddings = OpenAIEmbeddings()
        knowledge_base = FAISS.from_texts(chunks, embeddings)  # "FlatL2")

    # show user input
    user_question = st.text_input("Ask a question about your PDF:")

    if pdf and user_question:
        docs = knowledge_base.similarity_search(user_question)

        llm = OpenAI()  # openai_api_key=openai_api_key)
        chain = load_qa_chain(llm, chain_type="stuff")
        with get_openai_callback() as cb:
            response = chain.run(input_documents=docs, question=user_question)
            print(cb)
        st.write(response)


if __name__ == "__main__":
    main()
