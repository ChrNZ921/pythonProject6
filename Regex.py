import re
import BaseDeDonnées


def decoder_message(message) :
    # Recherche sur expression régulière
    r = r'imei:(?P<imei>\d+),(?P<type>\w+),(?P<date>\d{6})\d{6},(?P<statut>.),(?P<heure>\d{6}.{3}),\w,(?P<latitude>\d{4}.{6}),(?P<laty>\w),(?P<longitude>\d{5}.{6}),(?P<longy>\w)'
    m = re.match(r, message)

    # Extraction des matches dans un dictionnaire
    global d
    d = m.groupdict()

    # Nettoyage date/heure
    d['dateheure'] = re.sub(r"(\d{2})(\d{2})(\d{2})(\d{2})(\d{2})(\d{2})", "20\\1-\\2-\\3 \\4:\\5:\\6",
                            d['date'] + d['heure'][:6], 1)
    del d['date']
    del d['heure']
    # Nettoyage coordonnées
    d['latitude'] = calculer_coordonnees(d['latitude'], d['laty'])
    d['longitude'] = calculer_coordonnees(d['longitude'], d['longy'])
    del d['laty']
    del d['longy']

    return d


def calculer_coordonnees(dms, ori) :
    sep = 2 if ori == 'N' or ori == 'S' else 3
    deg = int(dms[:sep])
    min = float(dms[sep :])
    sgn = 1 if ori == 'N' or ori == 'E' else -1

    result = sgn * (deg + min / 60)

    return result

