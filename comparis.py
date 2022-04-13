from bs4 import BeautifulSoup
import requests
import xml.etree.ElementTree as ET

url = 'https://it.comparis.ch/immobilien/api/v1/singlepage/resultitems?requestObject={%22Header%22:{%22Language%22:%22it%22},%22SearchParams%22:{%22DealType%22:20,%22SiteId%22:0,%22RootPropertyTypes%22:[],%22PropertyTypes%22:[],%22RoomsFrom%22:null,%22RoomsTo%22:null,%22FloorSearchType%22:0,%22LivingSpaceFrom%22:null,%22LivingSpaceTo%22:null,%22PriceFrom%22:null,%22PriceTo%22:null,%22ComparisPointsMin%22:0,%22AdAgeMax%22:0,%22AdAgeInHoursMax%22:null,%22Keyword%22:%22%22,%22WithImagesOnly%22:null,%22WithPointsOnly%22:null,%22Radius%22:null,%22MinAvailableDate%22:%221753-01-01T00:00:00%22,%22MinChangeDate%22:%221753-01-01T00:00:00%22,%22LocationSearchString%22:%22Zurich%22,%22Sort%22:3,%22HasBalcony%22:false,%22HasTerrace%22:false,%22HasFireplace%22:false,%22HasDishwasher%22:false,%22HasWashingMachine%22:false,%22HasLift%22:false,%22HasParking%22:false,%22PetsAllowed%22:false,%22MinergieCertified%22:false,%22WheelchairAccessible%22:false,%22LowerLeftLatitude%22:null,%22LowerLeftLongitude%22:null,%22UpperRightLatitude%22:null,%22UpperRightLongitude%22:null},%22Page%22:0}'
singlePageUrl = 'https://it.comparis.ch/immobilien/marktplatz/details/show/27643909'
prefix = 'https://it.comparis.ch/immobilien/marktplatz/details/show/'
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


def scrapePage(url):
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, 'lxml')
    meterSquare = soup.find('h3', class_='css-yidf68 ehesakb2')
    price = soup.find('h3', class_='css-eujsoq ehesakb2')
    address = soup.find('h5', class_='css-15z12tn ehesakb2')
    mainFeatures = soup.findAll('div', class_='css-1jy9b6z ehesakb4')
    description = soup.find('div', class_='css-16i3sck ehesakb2')
    print(meterSquare.text)
    print(price.text)
    print(address.text)
    for feature in mainFeatures:
        print(feature.text + " ")
    if description is not None: print(description.text)
    # print(soup)


def getLinksInPage(url):
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, 'lxml')
    result = str((soup.adidlist))
    tree = ET.fromstring(result)
    for child in tree:
        link = (prefix + str(child.text))
        print(link)
        scrapePage(link)
        print('\n')

getLinksInPage(url)
