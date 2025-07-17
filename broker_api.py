import requests

class BrokerAPI:
    """ارتباط امن با بروکر و مدیریت سفارشات"""
    def __init__(self, api_host, api_token):
        self.api_host = api_host
        self.api_token = api_token

    def _headers(self):
        return {"Authorization": f"Bearer {self.api_token}"}

    def place_order(self, symbol, volume, side):
        """ارسال سفارش خرید/فروش"""
        payload = {
            "symbol": symbol,
            "volume": volume,
            "side": side
        }
        response = requests.post(
            f"{self.api_host}/order",
            json=payload,
            headers=self._headers()
        )
        return response.json()

    def account_balance(self):
        """دریافت موجودی فعلی حساب"""
        response = requests.get(
            f"{self.api_host}/balance",
            headers=self._headers()
        )
        return response.json()
