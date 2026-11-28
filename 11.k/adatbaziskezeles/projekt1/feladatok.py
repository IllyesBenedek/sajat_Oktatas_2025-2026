diakok = [
 {"nev": "Zuhany Rózsa",
  "osztaly": "11.C",
  "targy": "Adatbázisok",
  "jegy": [1, 2, 3, 3, 5, 5, 5]
  },
 {"nev": "Bevíz Elek",
  "osztaly": "11.A",
  "targy": "Adatbázisok",
  "jegy": [1, 2, 3, 3, 4, 1, 1]
  },
 {"nev": "Zsíros B. Ödön",
  "osztaly": "11.C",
  "targy": "Adatbázisok",
  "jegy": [1, 2, 3, 1, 1, 1, 1]
  },
 {"nev": "Ba Szonja",
  "osztaly": "11.A",
  "targy": "Adatbázisok",
  "jegy": [4, 5, 3]}]


szotar = {
    "nev": "Légy Ottó",
    "osztaly": "11.C",
    "targy": "Adatbazisok",
    "jegy": [1, 1, 1, 1, 3, 4]
    }


for elem in diakok:
    print(elem["nev"], "-", elem["osztaly"])


def atlag_szamitas(jegyek):
    ossz = sum(jegyek)
    elosztas = ossz / len(jegyek)
    return round(elosztas, 2)


print(atlag_szamitas(diakok[0]["jegy"]))


legmagasabb_atlag = 0
nev = ""

for elem in diakok:
    atlag = atlag_szamitas(elem["jegy"])
    if atlag > legmagasabb_atlag:
        legmagasabb_atlag = atlag
        nev = elem["nev"]
print(nev)
print(legmagasabb_atlag)
