import requests
from bs4 import BeautifulSoup
import csv


class Company(object):
    def __init__(self, id, name, nse_sym, rating, sector) -> None:
        self.__id = id
        self.__name = name
        self.__nsesym = nse_sym
        self.__rating = rating
        self.__sector = sector

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    @property
    def nse_sym(self):
        return self.__nsesym

    @property
    def rating(self):
        return self.__rating

    @property
    def sector(self):
        return self.__sector

    @property
    def comment(self):
        return self.__comment

    def setComment(self, text):
        self.__comment = text


user_input = "PI Industries"

user_input = "+".join(user_input.split(" "))


r2 = requests.get(
    "https://www.samco.in/knowledge-center/articles/best-agriculture-stocks-to-buy-in-india/")
soup2 = BeautifulSoup(r2.text, 'html.parser')
l = list(filter(None, soup2.text.split("\n")))[235:319]
c = []
for i in range(12):
    c.append(Company(l[7*i+0], l[7*i+1], l[7*i+3], l[7*i+5], l[7*i+6]))


for i in range(len(c)):
    url = "https://www.bing.com/news/search?q=" + \
        "+".join(c[i].name.split(" "))+"+india&FORM=HDRSC6"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    c[i].setComment(soup.text[350:])


filename = 'companies.csv'
with open(filename, 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    for item in c:
        print([item.id, item.name, item.rating,
               item.sector, item.comment])
        writer.writerow([item.id, item.name, item.rating,
                        item.sector, item.comment])
