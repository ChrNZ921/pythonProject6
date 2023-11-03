import re

m = re.match(r'imei:(?P<imei>\d+),(?P<type>\w+),(?P<date>\d{6})(?P<time>\d{6}),(?P<statut>.),(?P<heure>\d{6}.{3}),\w,(?P<latitude>\d{4}.{6}),(?P<laty>\w),(?P<longitude>\d{5}.{6}),(?P<longy>\w)','imei:864895031562505,tracker,231031121212,F,121212.00,A,0022.97401,S,00927.26038,E,')
print(m.groupdict())


def calculer_latitude(m):
    loc = re.search(r'^\d{2}', m.group("latitude"))
    lat = re.search(r'\d{2}.\d{5}', m.group("latitude"))

    loc = int(loc.group())
    lat = float(lat.group())

    lat = lat / 60
    ind = m.group("laty")
    result = loc + lat
    if ind == "N":
        print(f'la latitude est de : {result} Nord')
    else:
        print(f'la latitude est de : {-result} Sud')
def calculer_longitude(m):
    loc = re.search(r'^\d{3}', m.group("longitude"))
    lon = re.search(r'\d{2}.\d{5}', m.group("longitude"))

    loc = int(loc.group())
    lon = float(lon.group())

    lon = lon / 60
    result = loc + lon
    ind = m.group("longy")
    if ind == "E":
        print(f'la latitude est de : {result} Est')
    else:
        print(f'la latitude est de : {-result} Ouest')
calculer_longitude(m)
calculer_latitude(m)