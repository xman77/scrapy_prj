import requests
from bs4 import BeautifulSoup

response = requests.get(f"https://travel.ettoday.net/category/%E6%A1%83%E5%9C%92/")
soup = BeautifulSoup(response.text,"html.parser")
result = soup.find("h3", itemprop="headline")
print(result.select_one("a"))

# print(soup.prettify())