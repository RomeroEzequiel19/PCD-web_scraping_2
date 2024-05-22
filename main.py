import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.bbc.com/mundo/topics/cyx5krnw38vt")

soup = BeautifulSoup(response.text, "html.parser")

results = soup.find_all("img")

for img in results:
    print(img)
