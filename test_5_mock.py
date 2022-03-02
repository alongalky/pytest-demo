from unittest.mock import MagicMock


def add_and_report(x, y, report_result):
    result = x + y
    report_result(result)


def test_report_gets_called():
    mock_report_function = MagicMock()

    add_and_report(2, 3, mock_report_function)

    mock_report_function.assert_called_with(5)


def get_bitcoin_price_string(bitcoin_price_feed):
    price = bitcoin_price_feed.get_price()

    return f"$ {price:.02f}"


def test_bitcoin_formatting():
    mock_price_feed = MagicMock()
    mock_price_feed.get_price.return_value = 44_018.30145

    result = get_bitcoin_price_string(mock_price_feed)

    assert result == "$ 44018.30"
