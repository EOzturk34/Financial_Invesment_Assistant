import yfinance as yf
from data.loaders.base_stock_loader import BaseStockLoader

class YahooFinanceLoader(BaseStockLoader):
    def get_stock_price(self, ticker):
        try:
            stock = yf.Ticker(ticker)
            price = stock.info.get("regularMarketPrice")
            return price
        except Exception as e:
            print(f"Error fetching price for {ticker}: {e}")
            return None
        
    def get_historical_prices(self, ticker, interval="daily", period="1mo"):
        interval_map={
            "daily": "1d",
            "weekly": "1wk",
            "monthly": "1mo"
        }
        yf_interval = interval_map.get(interval, "1d")
        try:
            stock = yf.Ticker(ticker)
            historical_data = stock.history(period=period, interval=yf_interval)
            return historical_data
        except Exception as e:
            print(f"Error fetching historical data for {ticker}: {e}")
            return None