import requests
from bs4 import BeautifulSoup as bs 

# need to add description - отличается от характеристики
def parse_allbazar_toys():  # парсинг игрушек с сайта allbazar.top и пропись товаров в csv или лучше json
    
    for page in range (1):
        url = f'https://allbazar.uz/cat/api/getcat.php?params%5Bfilter%5D%5BACTIVE%5D=Y&params%5Bfilter%5D%5B!PREVIEW_PICTURE%5D=false&params%5Bfilter%5D%5BINCLUDE_SUBSECTIONS%5D=Y&params%5Bfilter%5D%5BSECTION_ID%5D=103&params%5Bclass%5D=col-md-3%20mb-3%20col-20%20col-6&params%5Bsort%5D%5BSHOW_COUNTER%5D=DESC&params%5Bsort%5D%5BSECTION_ID%5D=RAND&params%5Bpagen%5D%5BnPageSize%5D=10&params%5Bpagen%5D%5BiNumPage%5D={page}'
        HEADERS = {'user_agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.146 Safari/537.36"}
        s = requests.session()
        r = requests.get(url, headers=HEADERS)
        soup = bs(r.content, 'lxml')
        # print(soup) - checkpoint
        list_item = soup.find_all('div', class_='col-md-3 mb-3 col-20 col-6')
        
    for item in list_item:
        draft_urls_list = []

        draft_urls = item.find('div', class_='listItem').find('a').get("href")
        draft_urls_list.append(draft_urls)
        # print(draft_urls_list)# - checkpoint
        for i in draft_urls_list:
            characteristics1 = []
            additional_photos = []
            final_urls = f'https://allbazar.uz' + i
            # print(final_urls) - #checkpoint  
            r = requests.get(final_urls).content
            soup = bs(r, 'lxml')
            main_img = soup.find('div', class_='col-10 position-relative').find('img').get('data-src')
            main_photo = 'https://allbazar.uz' + main_img
            dir = soup.find('div', class_="col-2").find_all('img')
            for i in dir:
                imgs = url + i['data-big']
                additional_photos.append(imgs)
            product_name = soup.find('h1', class_='h3 mb-3').get_text()  # DONE
            product_price = soup.find('span', class_='listPrice').get_text().replace('uzs',' сум')  # DONE - NEED TO TRY ADD MARGIN
            characteristics = soup.find('div', attrs='br-block p-3 bg-white')
            rows = characteristics.find_all(attrs='col-md-6')

            for row in rows:
                for characteristic in row.find_all('div'):
                    _ch = characteristic.text.strip('\n').strip('\t')
                    characteristics1.append(_ch)

        print(product_name,)
        print(product_price)
        print(characteristics1)
        print( main_photo,)
        print(additional_photos)

parse_allbazar_toys()


