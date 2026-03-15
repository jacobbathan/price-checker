import yfinance as yf
import pandas as pd
import plotly.graph_objects as go

def main():
    print("Hello from stock-data-visualizer!\n")

    print("Enter the ticker symbol of the companies you'd like to see.")
    companies = retrieve_input()
    data = get_price_data(companies)
    df = clean_data(data.history(period="1y"))
    df = calculate_returns(df)
    plot_data(df)

def retrieve_input():
    ticker = input()
    return ticker

def get_price_data(ticker):
    if ticker.count(" ") > 1:
        data = yf.Tickers(ticker)
    else:
        data = yf.Ticker(ticker)
    return data

def clean_data(data):
    clean = data[["Close"]]
    clean = clean.dropna()
    return clean

def calculate_returns(data):
    new_data = data
    new_data["Returns"] = new_data["Close"].pct_change()
    new_data = new_data.dropna()
    return new_data

def plot_data(df):
    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x = df.index,
        y = df["Close"],
        name="Price"
    ))

    fig.add_trace(go.Scatter(
        x = df.index,
        y = df["Returns"],
        name="Returns"
    ))
    
    fig.show()

if __name__ == "__main__":
    main()
