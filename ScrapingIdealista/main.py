# TO DO:
# 1) trovare numero di pagine automaticamente
# 2) guarda codice di Deep

from bs4 import BeautifulSoup
import requests
import pandas as pd
import lxml

from fun import *

df = pd.DataFrame(columns=['title', 'size', 'place', 'price', 'link'])

max_pages = 5

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/100.0.4896.75 Safari/537.36',
    'Accept-Language': 'it-IT,it;q=0.9,en-US;q=0.8,en;q=0.7',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,'
              'application/signed-exchange;v=b3;q=0.9',
    'sec-ch-ua': '"Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1'
}

url_page = 'https://www.idealista.it/vendita-case/milano-milano/'


page_list = get_page_link(2)

for page in page_list:

    house_list = get_house_link(page)

    for house in house_list:

        new_row = scrape_page(house)

        df = df.append(new_row, ignore_index=True)

print(df)

