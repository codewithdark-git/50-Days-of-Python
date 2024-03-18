
import requests
from bs4 import BeautifulSoup

url = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"
header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}

response = requests.get(url, headers=header)

soup = BeautifulSoup(response.content, "html.parser")

# Find the title element
title_element = soup.find(id="productTitle", class_="a-size-large")

# Check if the title element exists
if title_element:
    # Extract the text if the element exists
    title = title_element.get_text().strip()
    print(title)
else:
    # Print a message if the title element is not found
    print("Title not found")

# Find the price element
price_element = soup.find(class_="a-offscreen")

# Check if the price element exists
if price_element:
    # Extract the text if the element exists
    price = price_element.get_text()
    price_without_currency = price.split("$")[1]
    price_as_float = float(price_without_currency)
    print(price_as_float)
else:
    # Print a message if the price element is not found
    print("Price not found")
