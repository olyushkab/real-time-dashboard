import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Fetch historical stock price data for DSX, GM, GNK stocks
start_date = "2023-01-01"
end_date = pd.Timestamp.now().strftime("%Y-%m-%d")
dsx = yf.download("DSX", start=start_date, end=end_date)
gm = yf.download("GM", start=start_date, end=end_date)
gnk = yf.download("GNK", start=start_date, end=end_date)

# Combine stock price data into a single dataframe
df = pd.concat([dsx["Close"], gm["Close"], gnk["Close"]], axis=1)
df.columns = ["DSX", "GM", "GNK"]


# Create a function to update the graph
def animate(i):
    ax.clear()
    ax.plot(df.index, df["DSX"], label="DSX")
    ax.plot(df.index, df["GM"], label="GM")
    ax.plot(df.index, df["GNK"], label="GNK")
    ax.set_title("Stock Price Fluctuations")
    ax.set_xlabel("Date")
    ax.set_ylabel("Price ($)")
    ax.legend()


# Create the graph
fig, ax = plt.subplots(figsize=(10, 5))
ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()
