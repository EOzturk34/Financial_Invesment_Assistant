import finnhub as fb
from base_stock_loader import BaseStockLoader
import time
from config import FINNHUB_API_KEY

class FinnhubLoader(BaseStockLoader):
    def __init__(self, api_key):
        self.client = fb.Client(api_key=api_key)

    def get_stock_price(self, ticker):
        try:
            quote = self.client.quote(ticker)
            return quote["c"]
        except Exception as e:
            print(f"Error fetching price for {ticker}: {e}")
            return None
        
    def get_historical_prices(self, ticker, interval="daily", period="1mo"):
        try:
            interval_map={
                "daily": "D",
                "weekly": "W",
                "monthly": "M"
            }
            finnhub_interval = interval_map.get(interval, "D")
            data = self.client.stock_candles(ticker, finnhub_interval, int(time.time()) - 3600, int(time.time()))
        
        except Exception as e:
            print(f"Error fetching historical data for {ticker}: {e}")
            return None