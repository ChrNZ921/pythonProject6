import re



text = 'imei:864895031562505,tracker,231031121212,F,121212.00,A,0022.97401,N,00927.26038,E,'
regex = r'imei:(\d+),(\w+),(\d{6})(\d{6}),(.),(\d{6}.\d{2}),(.),(\d{4}.\d{5}),(.),(\d{5}.\d{5}),(.)'
match = re.search(regex, text)
data = { 'imei': match.group(1), 'type': match.group(2), 'date': match.group(3), 'time': match.group(4), 'status': match.group(5), 'latitude': match.group(7) + ''  + match.group(8), 'longitude': match.group(9) + '' + match.group(10) }
print(data)
