from bs4 import BeautifulSoup as bs
url = 'https://allbazar.uz'
with open("product.html", encoding="utf8") as file:
    src = file.read()
    soup = bs(src, 'lxml')
    additional_photos=[]
    dir = soup.find('div', class_="col-2").find_all('img')
    for i in dir:
        imgs = url + i['data-big']
        additional_photos.append(imgs)

print(additional_photos)



