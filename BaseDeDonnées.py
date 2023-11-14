
import sqlite3
def base_de_donnes(d):

    #Crée une connexion à une base de données SQLite
    conn = sqlite3.connect('ma_base.db')

    # Crée un objet Cursor pour exécuter des requêtes SQL
    cur = conn.cursor()

    # Crée une table tracker avec les colonnes correspondant aux données du tracker GPS
    cur.execute("CREATE TABLE IF NOT EXISTS tracker (imei, type,latitude,longitude, dateheure,dt_now)")

    # Extrait les données du tracker GPS à partir du message de l'utilisateur

    # Insère les données du tracker GPS dans la table tracker
    cur.execute("INSERT INTO tracker VALUES (:imei, :type, :latitude,:longitude,:dateheure, datetime('now'))",d)
    # Valide les changements dans la base de données
    conn.commit()

# Sélectionne tous les enregistrements de la table tracker
    cur.execute("SELECT * FROM tracker")

# Affiche le premier enregistrement
    print(cur.fetchone())
    print("données insérées dans la base")

# Ferme la connexion à la base de données
    conn.close()

    return d

#print(base_de_donnes(d))