import requests
from bs4 import BeautifulSoup as bs
import json

# Добавить сверху блок кода, чтобы парсил ссылки с категориями, из них все что вытекает ниже, тем самым весь сайт

# # добавить маржу


product_ulr_list = []
products = []
HEADERS = {
    'user_agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.146 Safari/537.36"
}

count = 0
counter = 0
for page in range(0, 29):
    url = f'https://allbazar.uz/cat/api/getcat.php?params%5Bfilter%5D%5BACTIVE%5D=Y&params%5Bfilter%5D%5B!PREVIEW_PICTURE%5D=false&params%5Bfilter%5D%5BINCLUDE_SUBSECTIONS%5D=Y&params%5Bfilter%5D%5BSECTION_ID%5D=103&params%5Bclass%5D=col-md-3%20mb-3%20col-20%20col-6&params%5Bsort%5D%5BSHOW_COUNTER%5D=DESC&params%5Bsort%5D%5BSECTION_ID%5D=RAND&params%5Bpagen%5D%5BnPageSize%5D=10&params%5Bpagen%5D%5BiNumPage%5D={page}'
    r = requests.get(url, headers=HEADERS)
    soup = bs(r.content, 'lxml')
    goods = soup.find_all(class_='d-block')
    for i in goods:
        prd_raw_link = i.get('href')
        product_ulr_list.append('https://allbazar.uz' + prd_raw_link)

for i in product_ulr_list:
    try:
        product_pictures = []
        product_specs = []
        r = requests.get(i, headers=HEADERS)
        soup = bs(r.content, 'lxml')
        product_title = soup.find(class_='h3 mb-3').text
        product_price = soup.find('span', class_='listPrice').get_text().replace('uzs', '')
        product_description = soup.find_all(class_="mt-2")[-1].get_text().strip().replace('Allbazar / ', '').replace(
            ' ', ' ')
        characteristics = soup.find('div', attrs='br-block p-3 bg-white')
        rows = characteristics.find_all(attrs='col-md-6')

        for row in rows:
            for characteristic in row.find_all('div'):
                _ch = characteristic.text.strip('\n').strip('\t')
                product_specs.append(_ch)

        dir = soup.find('div', class_="col-2").find_all('img')
        for item in dir:
            imgs = 'https://allbazar.uz' + item['data-big']
            product_pictures.append(imgs)
        counter += 1
        product_dict = {
            'product_sku': f'albz{counter}',
            'category': 'Children',
            'sub_category': 'Toys',
            "sub_category_2": "",
            'product_title': product_title.replace('\n', '').replace('\t', ''),
            'product_price': product_price.replace('\n', '').replace('\t', ''),
            'product_description': product_description.replace('\n', '').replace('\t', ''),
            'product_cpecs': product_specs,
            'product_pics': product_pictures,
            'product_colors': '',
            'product_sizes': '',
            'product_stock': 2,
            'product_rating': 1
        }

        count += 1
        print(f'#{count}: {i} is done...')

        products.append(product_dict)

        with open('test.json', 'w', ) as json_file:
            json.dump(products, json_file, indent=4, ensure_ascii=False)

    except Exception:
        pass



