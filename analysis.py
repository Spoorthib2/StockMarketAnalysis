import numpy as np

def analyze_stock(df):

    average_close = np.mean(df['Close'])
    highest_price = np.max(df['High'])
    lowest_price = np.min(df['Low'])

    df['Daily Change'] = df['Close'] - df['Open']

    df['Percentage Change'] = (
        (df['Close'] - df['Open']) / df['Open']
    ) * 100

    print("\n--- Stock Analysis ---")
    print("Average Closing Price:", average_close)
    print("Highest Price:", highest_price)
    print("Lowest Price:", lowest_price)

    df['Moving Average'] = df['Close'].rolling(window=2).mean()
    
    report = open("reports/stock_report.txt", "w")

    report.write("===== STOCK ANALYSIS REPORT =====\n\n")

    report.write(f"Average Closing Price: {average_close}\n")
    report.write(f"Highest Price: {highest_price}\n")
    report.write(f"Lowest Price: {lowest_price}\n\n")

    report.write("Daily Changes:\n")
    report.write(str(df[['Date', 'Daily Change',
                        'Percentage Change']]))
    last_close = df['Close'].iloc[-1]
    first_close = df['Close'].iloc[0]

    if last_close > first_close:
        suggestion = "BUY"
    else:
        suggestion = "SELL"

    print("Suggestion:", suggestion)

    report.write("\n\nSuggestion: ")
    report.write(suggestion)
    report.close()
    return df