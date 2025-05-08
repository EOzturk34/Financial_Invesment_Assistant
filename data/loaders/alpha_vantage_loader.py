import requests
from config import ALPHA_VANTAGE_API_KEY
from data.loaders.base_stock_loader import BaseStockLoader
import time

class AlphaVantageLoader(BaseStockLoader):###
    def get_stock_price(self, ticker):
        url = "https://www.alphavantage.co/query"
        params = {
            "function": "GLOBAL_QUOTE",  ###
            "symbol": ticker, #
            "apikey": ALPHA_VANTAGE_API_KEY
        }
        response = requests.get(url, params=params)
        time.sleep(1.5)
        data = response.json()
        try:
            price = float(data["Global Quote"]["05. price"])###
            return price
        except (KeyError, ValueError):
            print("Error: Could not parse price from response.")
            return None
        
  
    def get_historical_prices(self, ticker, interval="daily", outputsize="compact"):
        function_map = {
            "daily" : "TIME_SERIES_DAILY",
            "weekly" : "TIME_SERIES_WEEKLY",
            "monthly" : "TIME_SERIES_MONTHLY"
        }
        function = function_map.get(interval, "TIME_SERIES_DAILY")
        url = "https://www.alphavantage.co/query"
        params = {
            "function" : function, 
            "apikey" : ALPHA_VANTAGE_API_KEY,
            "outputsize" : outputsize,
            "symbol" : ticker
        }
        response = requests.get(url, params=params)
        data = response.json()

        key_map = {
            "daily" : "Time Series (Daily)",
            "weekly"  : "Weekly Time Series",
            "monthly" : "Monthly Time Series"
        }

        time_series_key = key_map.get(interval, "Time Series (Daily)")
        
        try:
            return data[time_series_key]
        except KeyError:
            print(f"Error: Could not parse historical data from response!")
            return None
        

