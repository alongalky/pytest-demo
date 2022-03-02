import requests


def report_result(result):
    raise Exception("Shouldnt be called in a test")


def get_bitcoin_price():
    rates = requests.get("https://bitpay.com/api/rates").json()
    return next(item["rate"] for item in rates if item["code"] == "USD")
