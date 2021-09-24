from bs4 import BeautifulSoup as bs
url = 'https://allbazar.uz'
with open("product.html", encoding="utf8") as file:
    src = file.read()
    soup = bs(src, 'lxml')
    product_description = soup.find('div', class_='container mt-3').find('div', class_='mt-2').text
    print(product_description)



