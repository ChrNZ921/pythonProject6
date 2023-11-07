import re
import sqlite3

m = re.match(r'imei:(?P<imei>\d+),(?P<type>\w+),(?P<date>\d{6})(?P<time>\d{6}),(?P<statut>.),(?P<heure>\d{6}.{3}),\w,(?P<latitude>\d{4}.{6}),(?P<laty>\w),(?P<longitude>\d{5}.{6}),(?P<longy>\w)','imei:864895031562775,tracker,231031121212,F,121212.00,A,0022.97401,S,00927.26038,E,')
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



# Crée une connexion à une base de données SQLite
conn = sqlite3.connect('ma_base.db')

# Crée un objet Cursor pour exécuter des requêtes SQL
cur = conn.cursor()

# Crée une table tracker avec les colonnes correspondant aux données du tracker GPS
cur.execute("CREATE TABLE IF NOT EXISTS tracker (imei TEXT, type TEXT, date TEXT, time TEXT, heure TEXT, latitude TEXT, longitude TEXT)")

# Insère les données du tracker GPS dans la table tracker
cur.execute("INSERT INTO tracker VALUES ('864895031562505', 'tracker', '231031', '121212', '121212.00', '0022.97401', '00927.26038')")

# Valide les changements dans la base de données
conn.commit()

# Sélectionne tous les enregistrements de la table tracker
cur.execute("SELECT * FROM tracker")

# Récupère le premier enregistrement
row = cur.fetchone()

# Convertit le tuple en dictionnaire
data = dict(zip([c[0] for c in cur.description], row))

# Affiche le dictionnaire
print(data)

# Ferme la connexion à la base de données
conn.close()
