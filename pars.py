
import numpy

import requests
from bs4 import BeautifulSoup as BS

r = requests.get('https://pkgh.edu.ru/obuchenie/25.html')
html = BS(r.content, 'lxml')
page_all_font = html.find_all('font')




for el in page_all_font:
    a = el.text
    if a == '1-я':
        continue
    if a == '2-я':
        continue
    if a == '3-я':
        continue
    if a == '4-я':
        continue
    if a == '5-я':
        continue
    if a == '6-я':
        continue
    if a == '7-я':
        continue
    if a == 'Время':
        continue

    if a == 'Пары':
        continue

    if a == (''
             ''):
        continue

    print(a)
    print(type(a))




