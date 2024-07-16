# %% Imports
from pathlib import Path
from dotenv import load_dotenv
import os
import openai


import streamlit as st

# from PyPDF2 import PdfReader
from pypdf import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.chains.question_answering import load_qa_chain
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.llms import OpenAI
from langchain.callbacks import get_openai_callback



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
