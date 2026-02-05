from bs4 import BeautifulSoup
# from fake_useragent import UserAgent
import requests

class CarElement:
    def __init__(self, name, price, link, year):
        self.name = name
        self.price = price
        self.link = link
        self.year = year
    def __str__(self):
        return f"{self.name}|{self.year}|{self.price}|{self.link}"

class CarList:
    def __init__(self):
        self.carlist = []
    def append(self, CarElement):
        # while self.carlist.count(CarElement) != 10:
            try:
                if CarElement not in self.carlist:
                    self.carlist.append(CarElement)
            except Exception as e:
                print(e)
    def __iter__(self):
        return iter(self.carlist)

Cars = CarList()
linkrel = "https://auto.drom.ru"
req = requests.get(linkrel)
soup = BeautifulSoup(req.content, 'html.parser')

# парсинг объявлений с последующим заполнением экземпляров класса CarElement
# for l in soup.find_all('div'): #css-1f68fiz - div.class of a car
#     carname = None
#     carprice = None
#     carlink = None
#     caryear = None
#     try:
#         if 'css-1f68fiz' in l.attrs.get('class'):
#             carname, caryear = l.h3.text.strip().split(', ')
#             carlink = l.a.get('href')
#             carprice = l.find('div', class_='_1wx3rbx4').text.replace('₽', '').replace(' ', '')
#         if carname is not None:
#             Cars.append(CarElement(carname, carprice, carlink, caryear))
#     except Exception as e:
#         pass

# парсинг всех марок авто
brands = []
brands_links = []
a = soup.find_all("a", {"class": "frg44i6"})
for i in a:
    brands.append(i.string.strip())
    brands_links.append(i.get("href"))
a = soup.find_all("noscript")
for i in a[0].prettify().split("</a>"):
    try:
        brands.append(i.split('/">\n  ')[1].strip())
        brands_links.append(i.split('href="')[1].strip().split('">\n')[0].strip())
    except Exception as e:
        pass

print(brands_links[50])
linkrel1 = brands_links[50]
req1 = requests.get(linkrel1)
soup1 = BeautifulSoup(req1.content, 'html.parser')
models = [model.text for model in soup1.find_all("a", {"class": "frg44i6"})]
models_links = [model.get("href") for model in soup1.find_all("a", {"class": "frg44i6"})]
if len(models) >= 19: # !!! очень жидко, не сработает, если в марке модели ровно 19 моделей !!! можно поменять на .contains()
    models += [model.text.split('/">')[0].strip() for model in soup1.find_all("noscript")[0]]
    models_links += [model.get("href").strip() for model in soup1.find_all("noscript")[0]]

for i in range(len(models)):
    print(f"{models[i]}|{models_links[i]}")


