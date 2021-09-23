from bs4 import BeautifulSoup as bs

with open("product.html", encoding="utf8") as file:
    src = file.read()
    soup = bs(src, 'lxml')
    dir = soup.find('div', class_='col-2').find('img').get('data-big')
    print(dir)