from bs4 import BeautifulSoup
import requests
import json


def scrapeData2(website):
    page = requests.get(website)
    soup = BeautifulSoup(page.content, 'lxml')
    titolo = soup.find('span', class_='im-titleBlock__title')
    prezzo = soup.find('div', class_='im-mainFeatures__title')
    locali = soup.findAll('span', class_='im-mainFeatures__value ')
    titoli = soup.findAll('dt', class_='im-features__title')
    valori = soup.findAll('dd', class_='im-features__value')
    print(website)
    print(titolo.text.lstrip())
    print("Prezzo " + prezzo.text.strip())
    # print("Locali: "+ locali.svg)
    for i, k in zip(titoli, valori):
        print(i.text.strip() + ": " + k.text.strip().replace("  ", "").replace("\n\n\n", ", "))
    print('\n')


def scrapeData(website):
    page = requests.get(website)
    soup = BeautifulSoup(page.content, 'lxml')
    links = soup.findAll('a', class_='in-card__title')
    for link in links:
        page = requests.get(link['href'])
        soup = BeautifulSoup(page.content, 'lxml')
        titolo = soup.find('span', class_='im-titleBlock__title')
        prezzo = soup.find('div', class_='im-mainFeatures__title')
        locali = soup.findAll('span', class_='im-mainFeatures__value ')
        titoli = soup.findAll('dt', class_='im-features__title')
        valori = soup.findAll('dd', class_='im-features__value')

        print(link['href'])
        print(titolo.text.lstrip())
        print("Prezzo " + prezzo.text.strip())
        # print("Locali: "+ locali.svg)
        for i, k in zip(titoli, valori):
            print(i.text.strip() + ": " + k.text.strip().replace("  ", "").replace("\n\n\n", ", "))
        print('\n')

#Get all the links in the url page and scrape the content of it
def getLinksInPage(url):
    page = requests.get(url)
    parsedContent = json.loads(page.content)
    #i is in the range 0 25, where 25 is the maximum links per page
    for i in range(0, len(parsedContent["results"]), 1):
        scrapeData2(parsedContent["results"][i]["seo"]["url"])
        links.append(parsedContent["results"][i]["seo"]["url"])


# the radius expressed in meters
radius = 1000
latitude = 45.5454787
longitude = 11.5354214
pageNumber = 1
links = []
urlProv = 'https://www.immobiliare.it/search-list/?raggio=' + str(radius) + '&centro=' + str(latitude) + '%2C' + str(
    longitude) + '&idContratto=1&idCategoria=1&criterio=rilevanza&ordine=desc&__lang=it&pag=1&slau=1'
# URL = 'https://www.immobiliare.it/vendita-case/milano-provincia/?criterio=rilevanza'
url = 'https://www.immobiliare.it/api-next/search-list/real-estates/?raggio=' + str(
    radius) + '&centro=' + str(latitude) + '%2C' + str(
    longitude) + '&idContratto=1&idCategoria=1&criterio=rilevanza&ordine=desc&__lang=it&pag=' + str(
    pageNumber) + '&paramsCount=9&path=%2Fsearch-list%2F'

page = requests.get(url)
parsedContent = json.loads(page.content)
maxPages = parsedContent["maxPages"]

getLinksInPage(url)

for i in range(1, maxPages, 1):
    pageNumber += 1
    url = 'https://www.immobiliare.it/api-next/search-list/real-estates/?raggio=' + str(
        radius) + '&centro=' + str(latitude) + '%2C' + str(
        longitude) + '&idContratto=1&idCategoria=1&criterio=rilevanza&ordine=desc&__lang=it&pag=' + str(
        pageNumber) + '&paramsCount=9&path=%2Fsearch-list%2F'
    getLinksInPage(url)
