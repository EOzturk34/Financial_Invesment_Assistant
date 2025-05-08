from abc import ABC, abstractmethod

class BaseStockLoader(ABC):
    @abstractmethod
    def get_stock_price(self, ticker):
        """Fetch the current stock price for the given ticker symbol."""
        pass

    @abstractmethod
    def get_historical_prices(self, tickers, interval="daily", outputsize="compact"):
        pass
