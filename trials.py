from bs4 import BeautifulSoup as bs
url = 'https://allbazar.uz'
with open("product.html", encoding="utf8") as file:
    src = file.read()
    soup = bs(src, 'lxml')

