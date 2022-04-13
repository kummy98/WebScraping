# load libraries
from bs4 import BeautifulSoup
import requests
import json
import pickle
from fun import *
import geopy
import geopy.distance


HEADERS = {
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

url = 'https://www.idealista.it/ajax/listingcontroller/livesearchmap.ajax?locationUri=&typology=1&o' \
      'peration=1&freeText=&liveSearch=true&zoom=16&northEast=45.45208275781088%2C+9.20756707023621' \
      '2&southWest=45.444857010779245%2C+9.1729129297638&uid=yk298widt7g0ropgx630dolk7vtndvt4l965nu' \
      'ebvl&adfilter_pricemin=default&adfilter_price=default&adfilter_area=default&adfilter_areamax=' \
      'default&adfilter_auctionability=default&adfilter_countryhouses=&adfilter_rooms_1=&adfilter_' \
      'rooms_2=&adfilter_rooms_3=&adfilter_rooms_4=&adfilter_rooms_5_more=&adfilter_baths_1=&adfilte' \
      'r_baths_2=&adfilter_baths_3=&adfilter_newconstruction=&adfilter_goodcondition=&adfilter_tobere' \
      'stored=&adfilter_hasairconditioning=&adfilter_wardrobes=&adfilter_lift=&adfilter_parkingspace=' \
      '&adfilter_garden=&adfilter_swimmingpool=&adfilter_hasterrace=&adfilter_boxroom=&adfilter_acces' \
      'sibleHousing=&adfilter_top_floor=&adfilter_intermediate_floor=&adfilter_ground_floor=&adfilter' \
      '_hasplan=&adfilter_digitalvisit=&adfilter_published=default&adfilter_onlyflats=&adfilter_penth' \
      'ouse=&adfilter_duplex=&adfilter_homes=&adfilter_independent=&adfilter_semidetached=&adfilter_t' \
      'erraced=&adfilter_villa=&adfilter_chalets='

clat = 45.4486468
clong = 9.1904216

nelat = 45.445
nelong = 9.18
swlat = 45.44486
swlong = 9.17291

ne = geopy.Point(nelat, nelong)
sw = geopy.Point(swlat, swlong)

distance = geopy.distance.distance(ne, sw).km

# ok so the area is calculated as follow, start from nelat and nelong and from them add dx and dy ∞
# where dy is how many km you do to the south and dx how many to the west
# so new_lat = lat + dy and new_long = long + dx


url_prova = 'https://www.idealista.it/ajax/listingcontroller/livesearchmap.ajax?locationUri=&typology=1&o' \
            'peration=1&freeText=&liveSearch=true&zoom=16&northEast='+str(nelat)+'%2C+'+str(nelong)+'' \
            '2&southWest='+str(swlat)+'%2C+'+str(swlong)+'&uid=yk298widt7g0ropgx630dolk7vtndvt4l965nu' \
            'ebvl&adfilter_pricemin=default&adfilter_price=default&adfilter_area=default&adfilter_areamax=' \
            'default&adfilter_auctionability=default&adfilter_countryhouses=&adfilter_rooms_1=&adfilter_' \
            'rooms_2=&adfilter_rooms_3=&adfilter_rooms_4=&adfilter_rooms_5_more=&adfilter_baths_1=&adfilte' \
            'r_baths_2=&adfilter_baths_3=&adfilter_newconstruction=&adfilter_goodcondition=&adfilter_tobere' \
            'stored=&adfilter_hasairconditioning=&adfilter_wardrobes=&adfilter_lift=&adfilter_parkingspace=' \
            '&adfilter_garden=&adfilter_swimmingpool=&adfilter_hasterrace=&adfilter_boxroom=&adfilter_acces' \
            'sibleHousing=&adfilter_top_floor=&adfilter_intermediate_floor=&adfilter_ground_floor=&adfilter' \
            '_hasplan=&adfilter_digitalvisit=&adfilter_published=default&adfilter_onlyflats=&adfilter_penth' \
            'ouse=&adfilter_duplex=&adfilter_homes=&adfilter_independent=&adfilter_semidetached=&adfilter_t' \
            'erraced=&adfilter_villa=&adfilter_chalets='

# "centreLat":45.4486468,
# "centreLong":9.1904216,
# "height":600,
# "items":[],
# "length":346,
# "northEastLat":45.45208,
# "northEastLong":9.20757,
# "southWestLat":45.44486,
# "southWestLong":9.17291,
# "width":940,
# "zoomLevel":15

print('url_prova: ' + url_prova)

page = requests.get(url_prova, headers=HEADERS)

print('page: ' + str(page))

parsedContent = json.loads(page.content)

print(parsedContent["jsonResponse"]["map"]["items"][0]["adId"])
print(parsedContent["jsonResponse"]["total"])

max_houses = parsedContent["jsonResponse"]["total"]

print(type(max_houses))

id_list = []
for i in range(int(max_houses)):
    id_list.append(parsedContent["jsonResponse"]["map"]["items"][i]["adId"])


print(id_list)

link_list = []
for i in id_list:
    link_list.append('https://www.idealista.it/immobile/' + str(i) +'/')

print(link_list)
print(len(link_list))

# with open("link_list", "wb") as fp:   #Pickling
#    pickle.dump(link_list, fp)

for house in link_list:
    scrape_page(house)