from urllib.request import urlopen
from bs4 import BeautifulSoup

alamat = "https://en.wikipedia.org/wiki/List_of_brightest_stars"
html = urlopen(alamat)
data = BeautifulSoup(html, 'html.parser')

table = data.findAll("table", {"class":"wikitable"})[0]
rows = table.findAll("tr")
for row in rows:
    for cell in row.findAll(["td", "th"]):
         print(cell.get_text())

hasil = []
for row in rows:
    info = []
    for cell in row.findAll(["td", "th"]):
        info.append(cell.get_text())
    hasil.append(info)