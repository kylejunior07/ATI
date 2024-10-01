import tkinter as tk
from tkinter import ttk
import requests
import random  # Import the random module

# This is the function to convert currency
def convert_currency():
    # This provides the URL for the Api
    url = f"https://api.exchangerate-api.com/v4/latest/{from_currency.get()}"
    # This is to send a request to the API to fetch the data needed for the conversion.
    response = requests.get(url)
    # This verifies whether the response from the API was successful.
    if response.ok:
        # Extract rates from the response
        rates = response.json().get('rates', {})
        # Gets the conversion rate for the selected currency
        rate = rates.get(to_currency.get(), 0)
        try:
            # This gets the amount entered by the user
            amount = float(amount_entry.get())
            if amount > 0:
                # Calculate the converted amount
                converted_amount = rate * amount
                # Display the converted amount with two decimal places
                result.set(f"{converted_amount:.2f}")
            else:
                result.set("Invalid input. Must be a positive number.")
        except ValueError:
            result.set("Invalid input.")
    else:
        result.set("Error fetching conversion.")

# This function shuffles currencies
def shuffle_currencies():
    # List of currencies
    currencies = ["USD", "EUR", "GBP", "JPY", "CAD", "INR", "NGN", "AUD", "CHF", "CNY", "SEK", "NZD", "MXN", "SGD", "HKD", "NOK", "KRW", "TRY", "RUB", "BRL", "ZAR", "AED", "SAR", "THB", "MYR", "DKK", "CZK", "EGP", "RON", "VND", "UAH", "PKR", "QAR", "TND", "HRK", "CRC"]
    # Shuffle the currencies randomly
    random.shuffle(currencies)
    # Assign new currencies for conversion
    from_currency.set(currencies[0])
    to_currency.set(currencies[1])

# Arrange the window layout according to the specified design.
root = tk.Tk()
root.title("Currency Converter")
root.geometry("400x400")
root.configure(bg="#1e3d59")

# Style configuration
style = ttk.Style()
style.configure('TLabel', font=('Helvetica', 12), background="#1e3d59", foreground="white")
style.configure('TButton', font=('Helvetica', 12), background='#2c3e50', foreground="red")
style.map('TButton', background=[('active', '#e74c3c')])
style.configure('TEntry', font=('Helvetica', 12), padding=10)
style.configure('TCombobox', font=('Helvetica', 12), padding=10)

# Variables
from_currency = tk.StringVar()
to_currency = tk.StringVar()
result = tk.StringVar()
amount_entry = ttk.Entry(root, font=('Helvetica', 12))
amount_entry.grid(column=1, row=0, sticky="ew", padx=10, pady=5)

# Dropdown for FROM currency
from_currency.set("USD")
from_currency_dropdown = ttk.Combobox(root, textvariable=from_currency, state="readonly", font=('Helvetica', 13))
from_currency_dropdown['values'] = ("USD", "EUR", "GBP", "JPY", "CAD", "INR", "NGN", "AUD", "CHF", "CNY", "SEK", "NZD", "MXN", "SGD", "HKD", "NOK", "KRW", "TRY", "RUB", "BRL", "ZAR", "AED", "SAR", "THB", "MYR", "DKK", "CZK", "EGP", "RON", "VND", "UAH", "PKR", "QAR", "TND", "HRK", "CRC")
from_currency_dropdown.grid(column=1, row=1, sticky="ew", padx=10, pady=5)

# Dropdown for TO currency
to_currency.set("EUR")
to_currency_dropdown = ttk.Combobox(root, textvariable=to_currency, state="readonly", font=('Helvetica', 13))
to_currency_dropdown['values'] = ("USD", "EUR", "GBP", "JPY", "CAD", "INR", "NGN", "AUD", "CHF", "CNY", "SEK", "NZD", "MXN", "SGD", "HKD", "NOK", "KRW", "TRY", "RUB", "BRL", "ZAR", "AED", "SAR", "THB", "MYR", "DKK", "CZK", "EGP", "RON", "VND", "UAH", "PKR", "QAR", "TND", "HRK", "CRC")
to_currency_dropdown.grid(column=1, row=2, sticky="ew", padx=10, pady=5)

# Convert button
convert_button = ttk.Button(root, text="Convert", command=convert_currency)
convert_button.grid(column=1, row=3, sticky="ew", padx=10, pady=10)
convert_button.configure(style='TButton')

# To handle currency shuffling.
shuffle_button = ttk.Button(root, text="Shuffle Currencies", command=shuffle_currencies)
shuffle_button.grid(column=0, row=3, sticky="ew", padx=10, pady=10)
shuffle_button.configure(style='TButton')

# To display the result.
result_label = ttk.Label(root, textvariable=result, font=('Helvetica', 12))
result_label.grid(column=1, row=4, sticky="ew", padx=10, pady=5)

# To create static labels within the graphical user interface to provide information or instructions to the user without the ability to interact with them.
ttk.Label(root, text="Amount:", font=('Helvetica', 12)).grid(column=0, row=0, padx=10, pady=5)
ttk.Label(root, text="From:", font=('Helvetica', 12)).grid(column=0, row=1, padx=10, pady=5)
ttk.Label(root, text="To:", font=('Helvetica', 12)).grid(column=0, row=2, padx=10, pady=5)
ttk.Label(root, text="Result:", font=('Helvetica', 12)).grid(column=0, row=4, padx=10, pady=5)

# This initiates the graphical user interface event loop to handle user interactions and keep the application responsive.
root.mainloop()

