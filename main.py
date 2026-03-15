import yfinance as yf
import pandas as pd
import plotly.graph_objects as go

def main():
    print("Hello from stock-data-visualizer!\n")

    print("Enter the ticker symbol of the companies you'd like to see.")
    companies = retrieve_input()
    data = get_price_data(companies)
    df = clean_data(data.history(period="1y"))

    df["Returns"] = df["Close"].pct_change()
    df = df.dropna()

    print(df)
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



if __name__ == "__main__":
    main()
