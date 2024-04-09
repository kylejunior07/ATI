#import tkinter as tk
import tkinter as tk
from tkinter import ttk
import requests

def convert_currency():
    # API URL for conversion
    url = f"https://api.exchangerate-api.com/v4/latest/{from_currency.get()}"
    
    # Make the request to the API
    response = requests.get(url)
    
    if response.ok:
        rates = response.json().get('rates', {})
        rate = rates.get(to_currency.get(), 0)
        try:
            amount = float(amount_entry.get())
            if amount > 0:  # Check if the amount is greater than 0
                converted_amount = rate * amount
                result.set(f"{converted_amount:.2f}")
            else:
                result.set("Invalid input. Amount must be greater than 0.")
        except ValueError:
            result.set("Invalid input.")
    else:
        result.set("Error fetching conversion.")

# Set up the window
root = tk.Tk()
root.title("Currency Converter")
root.geometry("400x400")  # Set initial size of the window

# Style configuration
style = ttk.Style()
style.configure('TLabel', font=('Arial', 10))
style.configure('TButton', font=('Arial', 10), background='#f0f0f0')
style.configure('TEntry', font=('Arial', 10), padding=10)
style.configure('TCombobox', font=('Arial', 10), padding=10)

# Variables
from_currency = tk.StringVar()
to_currency = tk.StringVar()
result = tk.StringVar()
amount_entry = ttk.Entry(root, font=('Arial', 12))
amount_entry.grid(column=1, row=0, sticky="ew", padx=10, pady=5)

# Dropdown for FROM currency
from_currency.set("USD") # Default value
from_currency_dropdown = ttk.Combobox(root, textvariable=from_currency, state="readonly", font=('Arial', 12))
from_currency_dropdown['values'] = ("USD", "EUR", "GBP", "JPY", "CAD", "INR", "NGN", "AUD", "CHF", "CNY", "SEK", "NZD", "MXN", "SGD", "HKD", "NOK", "KRW", " TRY)
from_currency_dropdown.grid(column=1, row=1, sticky="ew", padx=10, pady=5)

# Dropdown for TO currency
to_currency.set("EUR") # Default value
to_currency_dropdown = ttk.Combobox(root, textvariable=to_currency, state="readonly", font=('Arial', 12))
to_currency_dropdown['values'] = ("USD", "EUR", "GBP", "JPY", "CAD", "INR", "NGN", "AUD", "CHF", "CNY", "SEK", "NZD", "MXN", "SGD", "HKD", "NOK", "KRW", " TRY)
to_currency_dropdown.grid(column=1, row=2, sticky="ew", padx=10, pady=5)

# Convert button
convert_button = ttk.Button(root, text="Convert", command=convert_currency)
convert_button.grid(column=1, row=3, sticky="ew", padx=10, pady=10)

# Result label
result_label = ttk.Label(root, textvariable=result, font=('Arial', 12))
result_label.grid(column=1, row=4, sticky="ew", padx=10, pady=5)

# Static labels
ttk.Label(root, text="Amount:", font=('Arial', 12)).grid(column=0, row=0, padx=10, pady=5)
ttk.Label(root, text="From:", font=('Arial', 12)).grid(column=0, row=1, padx=10, pady=5)
ttk.Label(root, text="To:", font=('Arial', 12)).grid(column=0, row=2, padx=10, pady=5)
ttk.Label(root, text="Result:", font=('Arial', 12)).grid(column=0, row=4, padx=10, pady=5)

# Start the GUI event loop
root.mainloop()

