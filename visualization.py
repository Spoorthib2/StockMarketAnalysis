import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.widgets import RadioButtons

def plot_stock(df):
    """Show one month at a time, selected from the panel on the right."""
    plot_data = df.copy()
    plot_data['Month'] = plot_data['Date'].dt.to_period('M')
    available_months = sorted(plot_data['Month'].unique())

    if not available_months:
        raise ValueError("No dated stock data is available to plot.")

    fig, ax = plt.subplots(2, 1, figsize=(16, 8))
    fig.subplots_adjust(left=0.08, right=0.76, bottom=0.10, top=0.93, hspace=0.45)

    def format_dates():
        """Apply the existing date-label styling to both charts."""
        for axis in ax:
            axis.xaxis.set_major_locator(mdates.DayLocator(interval=5))
            axis.xaxis.set_major_formatter(mdates.DateFormatter('%d-%b'))
            axis.tick_params(axis='x', rotation=45)

        ax[0].tick_params(labelbottom=True)

    def draw_month(month):
        """Refresh both existing charts for the selected month."""
        month_data = plot_data[plot_data['Month'] == month]

        ax[0].clear()
        ax[1].clear()

        ax[0].plot(month_data['Date'], month_data['Close'], label="Closing Price")
        ax[0].plot(
            month_data['Date'],
            month_data['Moving Average'],
            label="Moving Average"
        )
        ax[0].set_title("Stock Closing Price Trend")
        ax[0].set_xlabel("Date")
        ax[0].set_ylabel("Price")
        ax[0].legend()

        ax[1].bar(month_data['Date'], month_data['Volume'])
        ax[1].set_title("Trading Volume")
        ax[1].set_xlabel("Date")
        ax[1].set_ylabel("Volume")

        format_dates()
        fig.canvas.draw_idle()

    month_labels = [month.strftime('%b %Y') for month in available_months]
    selector_axis = fig.add_axes([0.80, 0.10, 0.18, 0.80])
    selector_axis.set_title("Select Month", pad=10)
    month_selector = RadioButtons(selector_axis, month_labels, active=0)

    def select_month(label):
        draw_month(available_months[month_labels.index(label)])

    month_selector.on_clicked(select_month)
    draw_month(available_months[0])

    fig.savefig("graphs/full_report.png")

    plt.show()
