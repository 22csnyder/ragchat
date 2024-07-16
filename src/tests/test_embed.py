


import unittest
from unittest.mock import MagicMock, patch

import pytest

from ragchat.pdfchat import App, create_embeddings_from_reader


class TestCreateEmbeddingsFromReader:
    @patch('ragchat.pdfchat.PdfReader')
    @patch('ragchat.pdfchat.CharacterTextSplitter')
    @patch('ragchat.pdfchat.OpenAIEmbeddings')
    @patch('ragchat.pdfchat.FAISS')
    def test_create_embeddings_from_reader(self, mock_faiSS, mock_openAIEmbeddings, mock_characterTextSplitter, mock_pdfReader):
        # Setup mock objects
        mock_pdfReader.return_value.pages = [MagicMock(extract_text=lambda: "Page 1 Text"), MagicMock(extract_text=lambda: "Page 2 Text")]
        mock_characterTextSplitter.return_value.split_text.return_value = ["Chunk 1", "Chunk 2"]
        mock_openAIEmbeddings.return_value = MagicMock()
        mock_faiSS.from_texts.return_value = "FAISS Index Object"

        # Call the function
        result = create_embeddings_from_reader(mock_pdfReader())

        # Assertions
        mock_pdfReader.assert_called_once()
        mock_characterTextSplitter().split_text.assert_called_once_with("Page 1 TextPage 2 Text")
        mock_openAIEmbeddings.assert_called_once()
        mock_faiSS.from_texts.assert_called_once_with(["Chunk 1", "Chunk 2"], mock_openAIEmbeddings())
        assert result == "FAISS Index Object"