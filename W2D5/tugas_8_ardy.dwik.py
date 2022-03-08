#https://realpython.com/beautiful-soup-web-scraper-python/
import re
from unittest import result
import requests
from bs4 import BeautifulSoup

URL = "https://www.kompas.com/"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")
results = soup.find("div", class_="most__wrap clearfix")
#print(results)
berita = results.find_all("h4", class_="most__title")
print("Judul Berita Populer : ")
urutan = 0
for berita in berita:
    print(urutan,berita.text)
    print()
    urutan+=1