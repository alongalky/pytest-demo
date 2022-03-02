from unittest.mock import patch
import pytest


def add(x, y):
    return x + y


def test_cannot_add_string_and_float():
    with pytest.raises(TypeError):
        add(5, "hi")


class BitcoinException(Exception):
    pass


@pytest.fixture
def mock_get_bitcoin_price():
    with patch("utils.get_bitcoin_price") as mock:
        yield mock


def format_bitcoin_price():
    from utils import get_bitcoin_price

    try:
        price = get_bitcoin_price()
    except BitcoinException:
        return "Failed to get price. HODL on without me :("

    return f"$ {price:.02f}"


def test_patch_with_fixture(mock_get_bitcoin_price):
    mock_get_bitcoin_price.side_effect = BitcoinException()

    result = format_bitcoin_price()

    assert result == "Failed to get price. HODL on without me :("
