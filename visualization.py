import matplotlib.pyplot as plt

def plot_stock(df):

    fig, ax = plt.subplots(2, 1,
                           figsize=(8, 8))

    # First Graph
    ax[0].plot(df['Date'],
               df['Close'],
               label="Closing Price")

    ax[0].plot(df['Date'],
               df['Moving Average'],
               label="Moving Average")

    ax[0].set_title("Stock Closing Price Trend")

    ax[0].set_xlabel("Date")
    ax[0].set_ylabel("Price")

    ax[0].legend()

    # Second Graph
    ax[1].bar(df['Date'],
              df['Volume'])

    ax[1].set_title("Trading Volume")

    ax[1].set_xlabel("Date")
    ax[1].set_ylabel("Volume")

    plt.xticks(rotation=45)

    plt.tight_layout()

    plt.savefig("graphs/full_report.png")

    plt.show()