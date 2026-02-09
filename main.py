from bs4 import BeautifulSoup
# from fake_useragent import UserAgent
import requests

class CarElement:
    def __init__(self, name, price, link, year):
        self.name = name
        self.price = int(price)
        self.link = link
        self.year = year
    def __str__(self):
        return f"{self.name} | {self.year} | {self.price} | {self.link}"

class CarList:
    def __init__(self):
        self.carlist = []
        self.reverse = False
    def append(self, CarElement):
        try:
            if CarElement not in self.carlist:
                self.carlist.append(CarElement)
        except Exception as e:
            print(e)
    def sort(self, type_of_sort):
        match type_of_sort:
            case "year":
                if self.reverse:
                    self.carlist.sort(key=lambda x: x.year, reverse=True)
                    self.reverse = False
                else:
                    self.carlist.sort(key=lambda x: x.year, reverse=False)
                    self.reverse = True
            case "price":
                if self.reverse:
                    self.carlist.sort(key=lambda x: x.price, reverse=True)
                    self.reverse = False
                else:
                    self.carlist.sort(key=lambda x: x.price, reverse=False)
                    self.reverse = True

    def __iter__(self):
        return iter(self.carlist)

Cars = CarList()
linkrel = "https://auto.drom.ru/bmw/3-series/"
req = requests.get(linkrel)
soup = BeautifulSoup(req.content, 'html.parser')

# парсинг объявлений с последующим заполнением экземпляров класса CarElement
for l in soup.find_all('div', {'class':'css-1f68fiz'}): #css-1f68fiz - div.class of a car
    carname, caryear = l.h3.text.strip().split(', ')
    carlink = l.a.get('href')
    carprice = l.find('div', class_='_1wx3rbx4').text.replace('₽', '').replace(' ', '')
    if carname is not None:
        Cars.append(CarElement(carname, carprice, carlink, caryear))


# парсинг всех марок авто
linkrel1 = "https://auto.drom.ru/"
req1 = requests.get(linkrel1)
soup1 = BeautifulSoup(req1.content, 'html.parser')
brands = [brand.text for brand in soup1.find_all("a", {"class": "frg44i6"})]
brands_links = [brand.get("href") for brand in soup1.find_all("a", {"class": "frg44i6"})]
if len(brands) >= 19: # !!! очень жидко, не сработает, если в марке модели ровно 19 моделей !!! можно поменять на .contains()
    brands += [model.text.split('/">')[0].strip() for model in soup1.find_all("noscript")[0]]
    brands_links += [model.get("href").strip() for model in soup1.find_all("noscript")[0]]
for i in range(len(brands)):
    print(brands[i], brands_links[i])
#
# print(brands_links[50])
# linkrel1 = brands_links[50]
# req1 = requests.get(linkrel1)
# soup1 = BeautifulSoup(req1.content, 'html.parser')
# models = [model.text for model in soup1.find_all("a", {"class": "frg44i6"})]
# models_links = [model.get("href") for model in soup1.find_all("a", {"class": "frg44i6"})]
# if len(models) >= 19: # !!! очень жидко, не сработает, если в марке модели ровно 19 моделей !!! можно поменять на .contains()
#     models += [model.text.split('/">')[0].strip() for model in soup1.find_all("noscript")[0]]
#     models_links += [model.get("href").strip() for model in soup1.find_all("noscript")[0]]
#
# for i in range(len(models)):
#     print(f"{models[i]}|{models_links[i]}")


