import requests
from bs4 import BeautifulSoup

name = "Deepak Fertilisers and Petrochemicals Corporation"
r2 = requests.get(
    "https://www.bing.com/news/search?q=" +
    "+".join(name.split(" "))+"+india&FORM=HDRSC6")
soup2 = BeautifulSoup(r2.text, 'html.parser')
l = soup2.text[350:]
print(l)
