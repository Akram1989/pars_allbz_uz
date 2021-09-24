from bs4 import BeautifulSoup as bs


url = 'https://allbazar.uz'
with open("product.html", encoding="utf8") as file:
    src = file.read()
    soup = bs(src, 'lxml')
    characteristics1 = []
    additional_photos = []
    # final_urls = f'https://allbazar.uz' + i
    # print(final_urls) - #checkpoint
    soup = bs(src, 'lxml')
    main_img = soup.find('div', class_='col-10 position-relative').find('img').get('data-src')
    main_photo = 'https://allbazar.uz' + main_img
    dir = soup.find('div', class_="col-2").find_all('img')
    for i in dir:
        imgs = url + i['data-big']
        additional_photos.append(imgs)
    product_name = soup.find('h1', class_='h3 mb-3').get_text()  # DONE
    product_price = soup.find('span', class_='listPrice').get_text().replace('uzs',
                                                                             ' сум')  # DONE - NEED TO TRY ADD MARGIN
    characteristics = soup.find('div', attrs='br-block p-3 bg-white')
    rows = characteristics.find_all(attrs='col-md-6')

    for row in rows:
        for characteristic in row.find_all('div'):
            _ch = characteristic.text.strip('\n').strip('\t')
            characteristics1.append(_ch)

print(product_name, )
print(product_price)
print(characteristics1)
print(main_photo, )
print(additional_photos)




