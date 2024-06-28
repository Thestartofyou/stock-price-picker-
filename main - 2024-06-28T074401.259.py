import yfinance as yf
import matplotlib.pyplot as plt

def fetch_stock_data(ticker, period='1mo', interval='1d'):
    """
    Fetches historical stock data for a given ticker symbol.

    Parameters:
    ticker (str): The ticker symbol of the stock.
    period (str): The period of data to fetch (e.g., '1d', '5d', '1mo', '3mo', '6mo', '1y', '2y', '5y', '10y', 'ytd', 'max').
    interval (str): The interval between data points (e.g., '1m', '2m', '5m', '15m', '30m', '60m', '90m', '1d', '5d', '1wk', '1mo', '3mo').

    Returns:
    pandas.DataFrame: A DataFrame containing the historical stock data.
    """
    stock = yf.Ticker(ticker)
    data = stock.history(period=period, interval=interval)
    return data

def plot_stock_data(data, ticker):
    """
    Plots the closing price of the stock over time.

    Parameters:
    data (pandas.DataFrame): The historical stock data.
    ticker (str): The ticker symbol of the stock.
    """
    plt.figure(figsize=(10, 5))
    plt.plot(data.index, data['Close'], label='Close Price')
    plt.title(f'{ticker} Stock Price')
    plt.xlabel('Date')
    plt.ylabel('Price (USD)')
    plt.legend()
    plt.grid(True)
    plt.show()

def main():
    ticker = input("Enter the stock ticker symbol (e.g., AAPL, GOOGL, MSFT): ")
    period = input("Enter the period (e.g., '1mo', '3mo', '1y', '5y', 'max'): ")
    interval = input("Enter the interval (e.g., '1d', '1wk', '1mo'): ")

    data = fetch_stock_data(ticker, period, interval)
    plot_stock_data(data, ticker)

if __name__ == "__main__":
    main()
