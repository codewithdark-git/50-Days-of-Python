import requests
from bs4 import BeautifulSoup

def get_search_results(search_query):
    url = f"https://www.amazon.com/s?k={search_query}"
    header = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
        "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
    }
    response = requests.get(url, headers=header)
    soup = BeautifulSoup(response.content, "html.parser")
    return soup

def extract_product_info(search_results):
    products = []
    results = search_results.find_all("div", class_="s-result-item")
    for result in results:
        title_element = result.find("span", class_="a-size-medium")
        price_element = result.find("span", class_="a-price")
        if title_element and price_element:
            title = title_element.get_text().strip()
            price = price_element.find("span", class_="a-offscreen").get_text().strip()
            products.append({"title": title, "price": price})
    return products

def main():
    search_query = input("Enter your search query: ")
    search_results = get_search_results(search_query)
    products = extract_product_info(search_results)
    for idx, product in enumerate(products, start=1):
        print(f"Product {idx}:")
        print(f"Title: {product['title']}")
        print(f"Price: {product['price']}")
        print()

if __name__ == "__main__":
    main()
