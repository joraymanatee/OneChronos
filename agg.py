import pandas as pd

trades = pd.read_csv("data/trade_data_2024_04_01.csv")
quotes = pd.read_csv("data/quote_data_2024_04_01.csv")

print(trades.columns)
print(quotes.columns)

# Checking what it looks like
#trades.head()
#quotes.head()

trades["timestamp"] = pd.to_datetime(trades["transaction_timestamp"], unit="ns")
quotes["timestamp"] = pd.to_datetime(quotes["transaction_timestamp"], unit="ns")

# Adjusting based on price decimal to real price
trades["trade_price"] = trades["trade_price"] * (10.0 ** (-trades["price_decimal"]))
quotes["bid"] = quotes["bid_price"] * (10.0 ** (-quotes["price_decimal"]))
quotes["ask"] = quotes["ask_price"] * (10.0 ** (-quotes["price_decimal"]))

quotes = quotes.drop(columns=["bid_price", "ask_price"])

print(trades)

trades["ts_ns"] = trades["timestamp"].astype("int64")
quotes["ts_ns"] = quotes["timestamp"].astype("int64")

trades = trades.sort_values("ts_ns").reset_index(drop=True)
quotes = quotes.sort_values("ts_ns").reset_index(drop=True)

merged_data = pd.merge_asof(
    trades,
    quotes,
    on="ts_ns",
    by="symbol_id",
    direction="backward"
)

# Cleaning up data columns we don't really need.
merged_data = merged_data.drop(columns=[
    "transaction_timestamp_x",
    "transaction_timestamp_y",
    "price_decimal_x",
    "price_decimal_y",
    "ts_ns"
])

# Renaming for ease to read.
merged_data = merged_data.rename(columns={
    "timestamp_x": "trade_timestamp",
    "timestamp_y": "quote_timestamp"
})

merged_data.to_csv("merged_trades_with_nbbo.csv", index=False)
