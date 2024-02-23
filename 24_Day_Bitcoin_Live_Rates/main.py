import tkinter as tk
import ccxt
import time

# Initialize the Binance exchange (you can choose a different exchange)
exchange = ccxt.binance()

# List of common currency codes
common_currency_codes = ["USD", "EUR", "GBP", "USDT"]


# Create a function to update and display Bitcoin rates
def update_and_display_rates():
    try:
        # Fetch Bitcoin rates for various currencies
        btc_rates = {}
        for currency_code in common_currency_codes:
            symbol = f'BTC/{currency_code}'
            ticker = exchange.fetch_ticker(symbol)
            btc_rates[currency_code] = ticker['last']

        # Display the updated rates
        rate_text.config(state=tk.NORMAL)
        rate_text.delete(1.0, tk.END)  # Clear previous rates
        for currency_code, rate in btc_rates.items():
            rate_text.insert(tk.END, f"1 Bitcoin (BTC) = {rate} {currency_code}\n\n")

        # Apply some styling to the displayed text
        rate_text.tag_configure("center", justify="center")
        rate_text.tag_add("center", 1.0, "end")
        rate_text.config(state=tk.DISABLED)

    except Exception as e:
        rate_text.config(state=tk.NORMAL)
        rate_text.insert(tk.END, f"Error fetching rates: {str(e)}\n", "error")
        rate_text.config(state=tk.DISABLED)

    # Schedule the next update in 30 seconds
    root.after(300, update_and_display_rates)


# Create the main window
root = tk.Tk()
root.title("Bitcoin Exchange Rates")

# Create and place GUI components
# update_button = tk.Button(root, text="Update Rates", command=update_and_display_rates)
# update_button.pack()

rate_text = tk.Text(root, height=10, width=40, wrap=tk.NONE, font=13)
rate_text.pack()
rate_text.config(state=tk.DISABLED)

# Initial display of rates
update_and_display_rates()

# Start the main loop
root.mainloop()
