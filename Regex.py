import re

m = re.match(r'imei:(?P<imei>\d+),(?P<type>\w+),(?P<date>\d{6})(?P<time>\d{6}),(?P<statut>.),(?P<heure>\d{6}.{3}),\w,(?P<latitude>\d{4}.{6}),(?P<laty>\w),(?P<longitude>\d{5}.{6}),(?P<longy>\w)','imei:864895031562505,tracker,231031121212,F,121212.00,A,0022.97401,S,00927.26038,E,')
print(m.groupdict())


def calculer_coordonnees(m, coordonnee, loc_len, ind):

    #Recherche les différentes variables que l'on va utiliser
    loc = re.search(r'^\d{' + str(loc_len) + '}', m.group(coordonnee))
    val = re.search(r'\d{2}.\d{5}', m.group(coordonnee))

    #Transformes les chainnes de caractères e valleurs numériques
    loc = int(loc.group())
    val = float(val.group())

    #divise val par 60
    val = val / 60
    result = loc + val

    #determine le signe de nos coordonnées
    if ind == "N" or ind == "E":
        print(f'la {coordonnee} est de : {result} {ind}')
    else:
        print(f'la {coordonnee} est de : {-result} {ind}')

#rappel de la fonction et definition du nombre de chiffres que l'on va prendre au debut
calculer_coordonnees(m, "latitude", 2, m.group("laty"))
calculer_coordonnees(m, "longitude", 3, m.group("longy"))
