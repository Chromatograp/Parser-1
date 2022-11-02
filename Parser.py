import requests
from bs4 import BeautifulSoup
import json

#Адрес страницы, с которой будет происходить парсинг:
url = "http://health-diet.ru/table_calorie/?utm_source=leftMenu&utm_medium=table_calorie"

#Передаем заголовки в аргумент headers команды get, чтобы притвориться пользователем:
headers = {
    "Accept": "*/*",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:99.0) Gecko/20100101 Firefox/99.0"
}

req = requests.get(url, headers=headers)
src = req.text

#Записываем страницу в файл, чтобы не обращаться к сайту каждый раз и не получить бан за множество запросов:
with open("index.html", "w") as file:
    file.write(src)

#Читаем содержимое полученного файла:
with open("index.html") as file:
    src = file.read()

#Получаем содержимое класса mzr-tc-group-item-href:
soup = BeautifulSoup(src, "lxml")
all_products_href = soup.find_all(class_="mzr-tc-group-item-href")

#Получаем все ссылки с названиями:
all_categories_dict = {}
for item in all_products_href:
    item_text = item.text
    item_href = "http://health-diet.ru" + item.get("href")
    all_categories_dict[item_text] = item_href

# Записываем результат в json-файл:
with open("all_categories_dict.json", "w") as file:
    json.dump(all_categories_dict, file, indent=4, ensure_ascii=False)

