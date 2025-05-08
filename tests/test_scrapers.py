from data.loaders.stock_loader import get_stock_price_alpha_vantage

def test_get_stock_price():
    price = get_stock_price_alpha_vantage("AAPL")
    assert price is not None and price > 0
