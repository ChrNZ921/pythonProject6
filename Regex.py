import re

m = re.match(r'imei:(?P<imei>\d+),(?P<type>\w+),(?P<date>\d{6})(?P<time>\d{6}),(?P<statut>.),(?P<heure>\d{6}.{3}),\w,(?P<latitude>\d{4}.{6}),(?P<lat>\w),(?P<longitude>\d{5}.{6}),(?P<long>\w)','imei:864895031562505,tracker,231031121212,F,121212.00,A,0022.97401,N,00927.26038,E,')
print(m.groupdict())


def calculer_coordonnees(m):
    def calculer(coordonnee):
        loc = re.search(r'^\d{2,3}', m.group(coordonnee))
        val = re.search(r'\d{2}.\d{5}', m.group(coordonnee))

        loc = int(loc.group())
        val = float(val.group())

        val = val / 60
        result = loc + val

        return result

    latitude = calculer("latitude")
    longitude = calculer("longitude")

    print(f'la latitude est de : {latitude}')
    print(f'la longitude est de : {longitude}')

calculer_coordonnees(m)
