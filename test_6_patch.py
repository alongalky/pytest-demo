from unittest.mock import patch
import pytest


def format_bitcoin_price():
    from utils import get_bitcoin_price

    price = get_bitcoin_price()

    return f"$ {price:.02f}"


@patch("utils.get_bitcoin_price")
def test_bitcoin_formatting_is_pretty(mock_get_bitcoin_price):
    mock_get_bitcoin_price.return_value = 44_018.30145

    result = format_bitcoin_price()

    assert result == "$ 44018.30"


def test_patch_with_context_manager():
    with patch("utils.get_bitcoin_price") as mock_get_bitcoin_price:
        mock_get_bitcoin_price.return_value = 44_018.30145
        result = format_bitcoin_price()

    assert result == "$ 44018.30"


@pytest.fixture
def mock_get_bitcoin_price():
    with patch("utils.get_bitcoin_price") as mock:
        yield mock


def test_patch_with_fixture(mock_get_bitcoin_price):
    mock_get_bitcoin_price.return_value = 44_018.30145

    result = format_bitcoin_price()

    assert result == "$ 44018.30"
