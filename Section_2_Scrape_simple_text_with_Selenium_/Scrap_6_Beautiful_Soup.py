# Scrap currency with Beautiful Soup
from bs4 import BeautifulSoup
import requests

def get_currency(in_currency, out_currency, amount):
    url = f"https://www.x-rates.com/calculator/?from={in_currency}&to={out_currency}&amount={amount}"
    content = requests.get(url).text
    soup = BeautifulSoup(content, "html.parser")
    rate = soup.find("span", class_="ccOutputRslt").get_text()
    rate = float(rate[:-4])
    return in_currency, out_currency, amount, rate

# Get user inputs
in_currency = input("Enter the input currency (e.g., USD): ")
out_currency = input("Enter the output currency (e.g., EUR): ")
amount = float(input("Enter the amount: "))

# Call the function with user inputs
result = get_currency(in_currency, out_currency, amount)

# Access elements of the result tuple and display the result
print(f"The currency exchange for {result[0]} to {result[1]}, for {result[2]}{result[0]}, is {result[3]} {result[1]}")
