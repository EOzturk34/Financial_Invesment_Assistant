import sys
import os
import time
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from data.loaders.alpha_vantage_loader import AlphaVantageLoader
from data.loaders.yahoo_finance_loader import YahooFinanceLoader
from data.loaders.finnhub_loader import FinnhubLoader

data_sources = ["alpha_vantage"]
tickers = ["AAPL", "MSFT", "GOOGL"]
LOADER_MAP = {
    "alpha_vantage": AlphaVantageLoader,
    "yahoo_finance": YahooFinanceLoader,
    "finnhub_loader": FinnhubLoader
}

def get_loader(source):
   try:
       return LOADER_MAP[source]()
   except KeyError:
       raise ValueError(f"Unknown data source : {source}")
   
if __name__ == "__main__":
    data_sources = ["alpha_vantage", "yahoo_finance", "finnhub_loader"]
    tickers = ["AAPL", "MSFT", "GOOGL"]
    for source in data_sources:
        print(f"Results from {source}: ")
        try:
            if source == "finnhub_loader":
                 from config import FINNHUB_API_KEY
                 loader = FinnhubLoader(api_key=FINNHUB_API_KEY)
            else:
                loader = get_loader(source=source)

            for ticker in tickers:
                price = loader.get_stock_price(ticker)
                if price is not None:
                    print(f"{ticker}: ${price}")
                else:
                    print(f"Failed to fetch price for {ticker}.")
        except Exception as e:
            print(f"Error with {source}: {e}")
        print("\n")
        

