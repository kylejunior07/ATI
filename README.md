Name - Osmond Ezekwe
Kaplan ID - P428387
Introduction to Programming




Currency Converter Application

This Currency Converter application is a Python-based tool that enables users to convert currency from one type to another using the exchange rates provided by the exchangerate-api.com API. The Graphical User Interface (GUI) is constructed using the Tkinter library, which is a standard GUI toolkit for Python. This README will delve into the codebase, elucidate its functionalities, dependencies, installation steps, usage instructions, and provide insights into potential future enhancements.

Dependencies:
The Currency Converter application requires the following dependencies:

Python 3.x: The codebase is written in Python 3. Ensure you have Python installed on your system. If not, you can download and install it from the official Python website: https://www.python.org/downloads/
Tkinter: Tkinter is Python's de-facto standard GUI (Graphical User Interface) package. It comes pre-installed with Python, so no additional installation is necessary.

Requests: This library is used to make HTTP requests to the https://www.exchangerate-api.com/ API. 

Install it using pip:
pip install requests

Installation:
To install and run the Currency Converter application, follow these steps:
Clone the repository to your local machine:

git clone [repository URL]

Navigate to the directory containing the cloned repository:
cd currency-converter

Run the Python script currency_converter.py:
python currency_converter.py
API:
The program utilizes the ExchangeRate-API to fetch real-time currency exchange rates. It makes use of the free tier of this API. The API provides a simple endpoint to get exchange rates based on a specified base currency. In this code, we fetch the exchange rates based on the user-selected base currency and use it to perform currency conversion calculations.
rk requests and user inputs, to provide a robust user experience.


Code Explanation:
currency_converter.py: This is the main Python script that contains the application logic and GUI implementation.

Functionality:
Users can input the amount they want to convert, select the currency they want to convert from and to, and click the "Convert" button to get the converted amount.
The application fetches the latest exchange rates from the exchangerate-api.com API using the requests library.
Error handling is implemented to handle invalid input and API errors gracefully.

GUI Design:
The GUI is built using Tkinter widgets such as Labels, Entry, Combobox (Dropdown), and Button.
Styling is applied to the widgets using the ttk.Style() object to provide a modern and visually appealing interface.
The GUI layout is organized using the grid manager, which arranges widgets in a grid-like structure.

Usage:
To use the Currency Converter application, follow these steps:
Run the Python script currency_converter.py.
Enter the amount you want to convert in the "Amount" field.
Select the currency you want to convert from in the "From" dropdown menu.
Select the currency you want to convert to in the "To" dropdown menu.
Click the "Convert" or “Shuffle” button.
The converted amount will be displayed in the "Result" field.
Future Enhancements:
Here are some potential enhancements that could be made to the Currency Converter application:

Offline Mode: Implement a local currency exchange rate database to enable offline mode functionality.
Historical Rates: Add support for fetching historical exchange rates from the API.
Custom API Integration: Allow users to input their API key for accessing currency exchange rates from other providers.
Graphical Charts: Incorporate graphical charts to visualize currency trends and historical data.
Unit Testing: Write unit tests to ensure the reliability and stability of the application.

Contributing:
Contributions to the Currency Converter application are welcome! Feel free to submit bug reports, feature requests, or pull requests on GitHub: [[[link to GitHub repository]](https://github.com/kylejunior07/ATI-](https://github.com/kylejunior07/ATI-Currency-Conversion)



Author:
This Currency Converter application was developed by Osmond Ezekwe. If you have any questions or suggestions, please feel free to contact me at ezekwejunior@gmail.com.

Thank you for using the Currency Converter application! We hope it helps streamline your currency conversion needs.
