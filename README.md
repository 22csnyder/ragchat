# ragchat
## Intro
### A simple demo, using Retrieval Augmented Generation (RAG) and pdf utilities to create a chat interface one may use to ask questions of some laboratory documentation, protocols, or inventory data. (Some simple example data provided)


""" hello_rag_pdf.py            11/28/2023

    Summary:
    This is a document to test out simple knowledge retrieval from documents in simple cases. Also this is a first pass at langchain

    Notes:
    -In good working order 11/29/2023
    -Run in termainl with to view in browser localhost:8501 
    >>  streamlit run hello_rag_pdf.py

"""


## Setup



#conda create --name ragchat python=3.11
#conda env create --name ragchat python=3.9


conda create --name ragchat python=3.9
conda activate ragchat

pip install -U pip
pip install langchain python-dotenv openai streamlit pypdf 

streamlit run pdfchat.py





#pip install -e .



