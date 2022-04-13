from typing import Dict

from bs4 import BeautifulSoup
import requests
import idealista_costants as idc
from math import sin, cos, sqrt, atan2, radians, pi


import pandas as pd
import lxml

#
# url_base = 'https://www.idealista.it/vendita-case/milano-milano/'
#
# page = requests.get(url_base)
# soup = BeautifulSoup(page.content, 'lxml')
#
# links = soup.find_all('a', class_='item-link')
#
# link_list = []
#
# for link in links:
#     link_list.append(link["href"])
#
# print('link_list: ' + str(link_list))
#
# list_house_url = []
#
# for link in link_list:
#     url = 'https://www.idealista.it' + link
#     list_house_url.append(url)
#
# print('list_house_url: ' + str(list_house_url))


def get_page_link(max_pages):
    # input : number of desired pages (list)
    # output: a list containing all the url of the pages with list of houses

    # url_base = 'https://www.idealista.it/vendita-case/milano-milano/'
    url_list = []
    for i in range(1, max_pages):  # this is the list with all the pages url (1, 2, 3, 4, ... )
        url = idc.URL_BASE + 'lista-' + str(i) + '.htm'
        # print(url)
        url_list.append(url)
    return url_list


def get_house_link(url_page):
    # input: url of one page-list
    # output: list of all the house-url in the page

    page = requests.get(url_page, headers=idc.HEADERS)
    soup = BeautifulSoup(page.content, 'lxml')
    links = soup.find_all('a', class_='item-link')

    link_list = []

    for link in links:
        new_link = 'https://www.idealista.it/' + link["href"]
        link_list.append(new_link)

    return link_list


def scrape_page(url):
    # input: url of the house
    # output: row with all the desired info to insert in the df

    page = requests.get(url, headers=idc.HEADERS)
    soup = BeautifulSoup(page.content, 'lxml')
    print(url)
    title = soup.find('span', class_='main-info__title-main')
    title = title.get_text()
    print(title)
    place = soup.find('span', class_='main-info__title-minor')
    place = place.get_text()
    print(place)
    price = soup.find('span', class_='txt-bold')
    price = price.get_text()
    print(price + ' €')
    info = soup.find('div', class_='info-features')
    size = info.find('span').find('span')
    size = size.get_text()
    print(size + ' m^2')

    #new_row = {'title': title, 'size': size, 'place': place, 'price': price, 'link': url}
    #return new_row

#
# for house in list_house_url:
#     scrape_page(house)
#
# max_pages = 3




#
# df = pd.DataFrame(columns=['title', 'size', 'place', 'price'])
#
# url_list = get_page_link(max_pages)
#
# for url in url_list:
#     page = requests.get(url)
#     soup = BeautifulSoup(page.content, 'lxml')
#     links = soup.find_all('a', class_='item-link')
#
#     link_list = []
#
#     for link in links:
#         new_link = 'https://www.idealista.it/' + link["href"]
#         link_list.append(new_link)
#
#     for link in link_list:
#         print(link)
#         new_row = scrape_page(link)
#         df = df.append(new_row, ignore_index=True)
#
# print(df)

# https://www.idealista.it/vendita-case/milano-milano/lista-7.htm
# https://www.idealista.it/vendita-case/milano-milano/

def get_coord(lat, long, dx, dy):
    R = 6373.
    new_lat = lat + (dy / R) * (180 / pi)
    new_long = long + (dx / R) * (180 / pi) / cos(lat * pi / 180)
    return new_lat, new_long

