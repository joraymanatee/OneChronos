import pandas as pd

# Getting trade counts per exchange

data = pd.read_csv("data/merged_trades_with_nbbo.csv")
exchange_counts = data['trade_exchange_code'].value_counts()
print(exchange_counts)