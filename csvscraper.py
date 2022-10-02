from typing import List
from unicodedata import name
from bs4 import BeautifulSoup
import requests
import csv


categories = {
    "bse-healthcare_15": "healthcare",
    "bse-it_17": "IT",
    "bse-bankex_18": "banking",
    "bse-oil--gas_22": "oil&gas",
    "bse-metal_21": "steel&metal",
    "bse-auto_20": "Automobile",
    "bse-power_30": "Power",
    "bse-teck_10": "Tech",
}

url = "https://www.moneycontrol.com/stocks/marketstats/bse-gainer/"


class Company(object):
    def __init__(self, name, price, gain, sector) -> None:
        self.__name = name
        self.__price = price
        self.__gain = gain
        self.__sector = sector

    @property
    def name(self):
        return self.__name

    @property
    def price(self):
        return self.__price

    @property
    def gain(self):
        return self.__gain

    @property
    def sector(self):
        return self.__sector


companies = []

for ckey in categories.keys():
    finalURL = url+ckey+"/"
    try:
        r = requests.get(finalURL)
        soup = BeautifulSoup(r.text, 'html.parser')
        rows = soup.find("tbody").find_all("tr")

        for i in range(len(rows)):

            temp = [j.text for j in rows[i].select(
                "td.PR span.gld13.disin a")]
            if(len(temp) > 0):
                companies.append(Company(temp[0], rows[i].select(
                    "td")[1].text.replace(",", ""), rows[i].select("td")[6].text, categories[ckey]))

    except:
        print("Error fetching data")

filename = 'stocks.csv'
try:
    with open(filename, 'a', newline='') as f:
        writer = csv.writer(f)
        for item in companies:
            writer.writerow([item.name, item.price, item.gain, item.sector])
except BaseException as e:
    print('BaseException:', filename)
