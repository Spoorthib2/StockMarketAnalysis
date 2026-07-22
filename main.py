import pandas as pd

from analysis import analyze_stock
from visualization import plot_stock

df = pd.read_excel("data/stock_data.xlsx")

df['Date'] = pd.to_datetime(df['Date'])

print(df)

print("\nFirst Date:", df['Date'].min())
print("Last Date :", df['Date'].max())
print("Rows      :", len(df))

df = analyze_stock(df)

plot_stock(df)
