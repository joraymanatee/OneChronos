import pandas as pd

# Getting average sizes of bid and ask sizes for each symbol_id

data = pd.read_csv("quote_data_2024_04_01.csv")
data['average_bid_size'] = data['bid_size']
data['average_ask_size'] = data['ask_size']
relative_sizes = data.groupby('symbol_id').agg({
    'average_bid_size': 'mean',
    'average_ask_size': 'mean'
})

print(relative_sizes)