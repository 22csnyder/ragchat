import pytest

from ragchat.pdfchat import hello_world


@pytest.mark.hello_world
class TestInstall:
    def test_hello_world(self):
        from ragchat.pdfchat import hello_world
        assert hello_world() == "Hello World"
