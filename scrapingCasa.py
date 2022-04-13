from bs4 import BeautifulSoup
import requests
import re
import json


def scrapePage(url):
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, 'lxml')
    price = soup.find('li', class_='infos__list__price infos__list__price--wbtn')
    if price is None:
        price = soup.find('li', class_='infos__list__price infos__list__price--wbtn--auct')
    # localNumber = soup.find('li', class_='infos__list__item infos__list__item--mlast')
    metersSquare = soup.find('li', class_='infos__list__item')
    title = soup.find('h1', class_='infos__H1')
    description = soup.find('div', class_='descr__desc')
    featureList = soup.findAll('li', 'chars__feats__list--item')
    energeticClass = soup.find('p', class_='chars__ec--noclass')
    serviceList = soup.findAll('p', 'pois__grid--item')

    print(price.text)
    # print(localNumber.text)
    print(metersSquare.text)
    print(title.text)
    print(description.text.lstrip())
    for feature in featureList:
        print(feature.text.lstrip())
    if energeticClass is not None: print(energeticClass.text)
    for service in serviceList:
        print(service.text.lstrip())

def getLinksInPage(url):
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, 'lxml')
    linksPrefix = 'https://www.casa.it'
    links = soup.findAll('figure', class_='is-full-fit')
    for link in links:
        newLink = linksPrefix + link.a['href']
        print(newLink)
        scrapePage(newLink)


radius = 1000
latitude = 45.5454787
longitude = 11.5354214
pageNumber = 1
links = []

url = 'https://www.casa.it/srp/map/?tr=vendita&geocircle={%22circle%22:[{%22distance%22:835.102563591987,%22center%22:[45.09964641379579,9.986239633814824]}],%22bbox%22:[[45.114200793939304,9.951521120326055],[45.08508930860041,10.020958147303594]],%22zoom%22:15}&precision=6&propertyTypeGroup=case&surrounding=false'
url2 = 'https://www.casa.it/srp/?page='+str(pageNumber)+'&tr=vendita&geocircle={%22circle%22:[{%22distance%22:835.102563591987,%22center%22:[45.09964641379579,9.986239633814824]}],%22bbox%22:[[45.107471944821235,9.968119779922414],[45.09653665632228,9.994598547317434]],%22zoom%22:16}&precision=7&propertyTypeGroup=case&surrounding=false'
urlSinglePage = 'https://www.casa.it/immobili/43442487/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36',
    'Accept-Language': 'it-IT,it;q=0.9,en-US;q=0.8,en;q=0.7',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-ch-ua': '"Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1'
}
page = requests.get(url2, headers=headers)
soup = BeautifulSoup(page.content, 'lxml')
#print(page)
#print(soup)
url4= 'https://www.casa.it/portal-srp/api/v1/search-map/infobox'
request = {
    "apireq": {
        "site": "it_casa",
        "page": 1,
        "size": 1,
        "sort": [],
        "fgroup": "all",
        "query": [
            {
                "where": [
                    {
                        "geo": {
                            "distance": 835.102563591987,
                            "center": [
                                45.09964641379579,
                                9.986239633814824
                            ]
                        }
                    },
                    {
                        "geo": {
                            "bbox": [
                                [
                                    45.10162353515625,
                                    9.9810791015625
                                ],
                                [
                                    45.100250244140625,
                                    9.982452392578125
                                ]
                            ]
                        }
                    }
                ],
                "filters": {
                    "transaction.type": "vendita",
                    "property_type_group": "case",
                    "surrounding": "false"
                },
                "modifiers": {
                    "with_surroundings": 'false',
                    "geo_boolean_op": "AND",
                    "with_credipass": 'false',
                    "with_filters": 'false',
                    "with_poi": 'false'
                }
            }
        ],
        "aggregate": [
            "maps@7.300"
        ],
        "precision": 8
    },
    "queryFilters": {
        "page": 1,
        "tr": "vendita",
        "geocircle": "{\"circle\":[{\"distance\":835.102563591987,\"center\":[45.09964641379579,9.986239633814824]}],\"bbox\":[[45.10356287296514,9.967249631881714],[45.095156548518354,10.001968145370483]],\"zoom\":16}",
        "precision": "7",
        "propertyTypeGroup": "case",
        "surrounding": "false"
    },
    "domain": "casa.it",
    "locale": "it",
    "uri": "/srp/map/?tr=vendita&geocircle={\"circle\":[{\"distance\":835.102563591987,\"center\":[45.09964641379579,9.986239633814824]}],\"bbox\":[[45.10356287296514,9.967249631881714],[45.095156548518354,10.001968145370483]],\"zoom\":16}&precision=7&propertyTypeGroup=case&surrounding=false"
}
response4 = requests.post(url4, data=request)
print(response4.content)
linksPrefix = 'https://www.casa.it'
links = soup.findAll('figure', class_='is-full-fit')
for link in links:
    newLink = linksPrefix + link.a['href']
    #print(newLink)
    #scrapePage(newLink)
# print(len(links))
# print(soup)
data = re.search(r'window\.__INITIAL_STATE__ = JSON\.parse\(("{.*}")\);', page.text)[1]
# print(data)
data2 = json.loads(data)
data3 = json.loads(data2)
#print(data3)
totalPages = data3['agencySrp']['paginator']['totalPages']
#print(json.dumps(data3, indent=4))
# print(page.text)
# total pages il numero di pagine totali
#getLinksInPage(url2)

for i in range (1, totalPages, 1):
    pageNumber += 1
    url = url2 = 'https://www.casa.it/srp/?page='+str(pageNumber)+'&tr=vendita&geocircle={%22circle%22:[{%22distance%22:835.102563591987,%22center%22:[45.09964641379579,9.986239633814824]}],%22bbox%22:[[45.107471944821235,9.968119779922414],[45.09653665632228,9.994598547317434]],%22zoom%22:16}&precision=7&propertyTypeGroup=case&surrounding=false'
    #getLinksInPage(url)