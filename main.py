from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import requests
import csv

class CarElement:
    def __init__(self, name, price, link):
        self.name = name
        self.price = price
        self.link = link

carlist = []

linkrel = "https://auto.drom.ru/skoda/"
req = requests.get(linkrel, headers={'User-Agent': UserAgent().random})
soup = BeautifulSoup(req.content, 'html.parser')

for l in soup.find_all('div'): #css-1f68fiz - div.class of a car
    carname = ''
    carprice = ''
    carlink = ''
    try:
        if 'css-1f68fiz' in l.attrs.get('class'):
            # print(l.h3.text)
            # print(l.a.get('href'))
            carname = l.h3.text
            carlink = l.a.get('href')
        if 'css-1dkhqyq' in l.attrs.get('class'):
            # print(l.span.text.replace(' ', ''))
            carprice = l.span.text.replace(' ', '')
    except Exception as e:
        #print(e)
        pass
    if carname != '':
        carlist.append(CarElement(carname, carprice, carlink))
for car in carlist:
    print(car.name)