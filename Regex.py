import re

text =  'imei:864895031562505,tracker,231031121212,,F,121212.00,A,0022.97401,N,00927.26038,E,,'
dict = {'imei':'', 'type':'', 'dateHeure':'', 'heure':'', 'latitude':'', 'longitude':''}

imei = r'\d{15}'
type = r'(\,[a-zA-Z]+)'
dateHeure = r',(\d{12}),'
heure = r'\d{6}\.\d{2}'
latitude = r'[-+]?\d{1,2}\.\d{5}'
longitude = r'[-+]?\d{1,3}\.\d{5}'


dict['imei'] = re.search(imei, text).group()
dict['type'] = re.search(type, text).group()
dict['dateHeure'] = re.search(dateHeure, text).group()
dict['heure'] = re.search(heure, text).group()
dict['latitude'] = re.search(latitude, text).group()
dict['longitude'] = re.search(longitude, text).group()

print(dict)
