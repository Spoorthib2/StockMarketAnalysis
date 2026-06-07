import pandas as pd

from analysis import analyze_stock
from visualization import plot_stock

# Read Excel File
df = pd.read_excel("data/stock_data.xlsx")

# Display Data
print(df)

# Analyze Stock
df = analyze_stock(df)

# Plot Graph
plot_stock(df)