import pandas as pd

# Bid ask spread calculation

data = pd.read_csv("data/quote_data_2024_04_01.csv")
filtered_data = data[data['symbol_id'].isin([10407, 7614])]
filtered_data['spread'] = filtered_data['ask_price'] - filtered_data['bid_price']
spread_summary = filtered_data.groupby('symbol_id')['spread'].agg(['mean', 'min', 'max'])
print(spread_summary)