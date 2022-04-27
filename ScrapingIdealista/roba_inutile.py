
import idealista_costants as c
import geopy
import geopy.distance
from fun import *

# print(c.HEADERS)

nelat = 45.445
nelong = 9.18
swlat = 45.44486
swlong = 9.17291

ne = geopy.Point(nelat, nelong)
sw = geopy.Point(swlat, swlong)

distance = geopy.distance.distance(ne, sw).km
print(distance)

new_cord = get_coord(nelat, nelong, 50, 50)

new_p = geopy.Point(new_cord)

print(geopy.distance.distance(ne, new_p))
print(sqrt(50**2 + 50**2))

'''
Paolo was here 
'''