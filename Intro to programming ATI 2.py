#import necessary libraries
import tkinter as tk
from tkinter import ttk
import requests

# Function to convert currency
def convert_currency():
    # API URL for conversion
    url = f"https://api.exchangerate-api.com/v4/latest/{from_currency.get()}"
    
    # Make the request to the API
    response = requests.get(url)
    
    # Check if the response is successful
    if response.ok:
        # Extract rates from the response
        rates = response.json().get('rates', {})
        # Get the conversion rate for the selected currency
        rate = rates.get(to_currency.get(), 0)
        try:
            # Get the amount entered by the user
            amount = float(amount_entry.get())
            # Check if the amount is greater than 0
            if amount > 0:
                # Calculate the converted amount
                converted_amount = rate * amount
                # Display the converted amount with two decimal places
                result.set(f"{converted_amount:.2f}")
            else:
                # If amount is not positive, display error message
                result.set("Invalid input. Must be a positive number.")
        except ValueError:
            # If the entered value is not a valid number, display error message
            result.set("Invalid input.")
    else:
        # If there's an error fetching data from API, display error message
        result.set("Error fetching conversion.")

# Set up the window
root = tk.Tk()
root.title("Currency Converter")
root.geometry("400x400")  # Set initial size of the window
root.configure(bg="#1e3d59")  # Set background color to blue

# Style configuration
style = ttk.Style()

# Configure labels
style.configure('TLabel', font=('Helvetica', 12), background="#1e3d59", foreground="white")
# Configure buttons
style.configure('TButton', font=('Helvetica', 12), background='#2c3e50', foreground="white")
style.map('TButton', background=[('active', '#e74c3c')])  # Change background color on hover/active state
# Configure entries
style.configure('TEntry', font=('Helvetica', 12), padding=10)
# Configure comboboxes
style.configure('TCombobox', font=('Helvetica', 12), padding=10)

# Variables
from_currency = tk.StringVar()
to_currency = tk.StringVar()
result = tk.StringVar()
amount_entry = ttk.Entry(root, font=('Helvetica', 12))
amount_entry.grid(column=1, row=0, sticky="ew", padx=10, pady=5)

# Dropdown for FROM currency
from_currency.set("USD") # Default value
from_currency_dropdown = ttk.Combobox(root, textvariable=from_currency, state="readonly", font=('Helvetica', 13))
from_currency_dropdown['values'] = ("USD", "EUR", "GBP", "JPY", "CAD", "INR", "NGN", "AUD", "CHF", "CNY", "SEK", "NZD", "MXN", "SGD", "HKD", "NOK", "KRW", "TRY", "RUB", "BRL", "ZAR", "AED", "SAR", "THB", "MYR", "DKK", "CZK", "EGP", "RON", "VND", "UAH", "PKR", "QAR", "TND", "HRK", "CRC")
from_currency_dropdown.grid(column=1, row=1, sticky="ew", padx=10, pady=5)

# Dropdown for TO currency
to_currency.set("EUR") # Default value
to_currency_dropdown = ttk.Combobox(root, textvariable=to_currency, state="readonly", font=('Helvetica', 13))
to_currency_dropdown['values'] = ("USD", "EUR", "GBP", "JPY", "CAD", "INR", "NGN", "AUD", "CHF", "CNY", "SEK", "NZD", "MXN", "SGD", "HKD", "NOK", "KRW", "TRY", "RUB", "BRL", "ZAR", "AED", "SAR", "THB", "MYR", "DKK", "CZK", "EGP", "RON", "VND", "UAH", "PKR", "QAR", "TND", "HRK", "CRC")
to_currency_dropdown.grid(column=1, row=2, sticky="ew", padx=10, pady=5)

# Convert button
convert_button = ttk.Button(root, text="Convert", command=convert_currency)
convert_button.grid(column=1, row=3, sticky="ew", padx=10, pady=10)
convert_button.configure(style='TButton')  # Apply style to the button

# Result label
result_label = ttk.Label(root, textvariable=result, font=('Helvetica', 12))
result_label.grid(column=1, row=4, sticky="ew", padx=10, pady=5)

# Static labels
ttk.Label(root, text="Amount:", font=('Helvetica', 12)).grid(column=0, row=0, padx=10, pady=5)
ttk.Label(root, text="From:", font=('Helvetica', 12)).grid(column=0, row=1, padx=10, pady=5)
ttk.Label(root, text="To:", font=('Helvetica', 12)).grid(column=0, row=2, padx=10, pady=5)
ttk.Label(root, text="Result:", font=('Helvetica', 12)).grid(column=0, row=4, padx=10, pady=5)

# Start the GUI event loop
root.mainloop()
