# from unittest.mock import MagicMock, patch
import unittest

import pytest
import streamlit as st

pth_pdf = 'src/data/txfsn-on_apheresis.pdf'



from ragchat.pdfchat import App


class TestApp:
    def test_init(self):
        # pass
        app = App()


    # @patch('streamlit.file_uploader')
    # def test_user_uploads_pdf(mock_file_uploader):
    #     # Mock the return value of file_uploader to simulate a user uploading a PDF file
    #     with open('pth_pdf', 'rb') as pdf_file:
    #         mock_file_uploader.return_value = pdf_file

    #         app = App()
    #         app.pdf = st.file_uploader("Upload a PDF", type=["pdf"])

    #         # Assert that the file_uploader was called with the correct parameters
    #         mock_file_uploader.assert_called_once_with("Upload a PDF", type=["pdf"])
            
    #         # Assert that the app.pdf attribute is not None, indicating a file was uploaded
    #         assert app.pdf is not None

    # def test_user_input_pdf(self):
    #     app = App()
    #     app.pdf = st. ( pth_pdf
    #     assert app.pdf
    #     app.pdf = None



# class TestApp:

#     @patch('streamlit.file_uploader')
#     @patch('streamlit.text_input')
#     def test_app_initialization(self, mock_text_input, mock_file_uploader):
#         app = App()
#         assert app.pdf is mock_file_uploader.return_value
#         assert app.user_question is mock_text_input.return_value

#     @patch('ragchat.pdfchat.load_dotenv')
#     def test_load_dotenv(self, mock_load_dotenv):
#         app = App()
#         app.load_dotenv()
#         mock_load_dotenv.assert_called_once()

#     @patch('ragchat.pdfchat.st')
#     def test_style_page(self, mock_st):
#         app = App()
#         app.style_page()
#         mock_st.set_page_config.assert_called_once_with(page_title="Ask your PDF")
#         mock_st.header.assert_called_once_with("Ask your PDF 💬")