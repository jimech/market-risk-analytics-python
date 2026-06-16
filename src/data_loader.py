import yfinance as yf


def download_adjusted_close_prices(tickers, start_date, end_date=None):
    """
    Download adjusted closing prices for a list of tickers using yfinance.

    Parameters:
        tickers (list): List of asset tickers.
        start_date (str): Start date in YYYY-MM-DD format.
        end_date (str or None): End date in YYYY-MM-DD format. If None, uses latest available data.

    Returns:
        pandas.DataFrame: Adjusted closing prices.
    """
    price_data = yf.download(
        tickers,
        start=start_date,
        end=end_date,
        auto_adjust=True,
        progress=False
    )

    prices = price_data["Close"].copy()

    return prices.dropna()