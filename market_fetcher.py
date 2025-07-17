import requests

class MarketFetcher:
    """دریافت داده بازار از APIهای خارجی"""

    def __init__(self, base_url, api_key):
        self.base_url = base_url
        self.api_key = api_key

    def fetch_quotes(self, symbols=("EURUSD", "GBPUSD")):
        """دریافت رایگان آخرین قیمت جفت‌ارزها"""
        quotes = {}
        for symbol in symbols:
            url = f"{self.base_url}/quotes?symbol={symbol}&apikey={self.api_key}"
            response = requests.get(url)
            response.raise_for_status()
            quotes[symbol] = response.json()["price"]
        return quotes

    def fetch_history(self, symbol, interval="1h", limit=500):
        """دریافت داده تاریخی"""
        url = f"{self.base_url}/history?symbol={symbol}&interval={interval}&limit={limit}&apikey={self.api_key}"
        response = requests.get(url)
        response.raise_for_status()
        return response.json()["candles"]
