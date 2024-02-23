import requests
from bs4 import BeautifulSoup

url = 'https://www.tiktok.com/'
r = requests.get(url)

soup = BeautifulSoup(r.content, 'html.parser')
links = soup.find_all('a')

# Filter and print links related to "For You"
for link in links:
    href = link.get('href')
    if href and '/foryou' in href:
        print(href)

