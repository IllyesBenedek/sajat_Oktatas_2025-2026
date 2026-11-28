

alma = "alma"

lista = [1, 2, 3, 4, 5, 6, 7, "alma", True, False, None]

print(lista[0]),
print(lista[-1])
print(lista[7])
print(lista[3:8])


lista = []
szotar = {
    "nev": "Légy Otto",
    "anyja_neve": "Sunnya Mária",
    "Szuletesi_datum": "2003.06-.26",
    "eletkor": 17,
    "jegyek": [1, 1, 1, 1, 1, 1, 2, 2, 1]
    }

print(szotar["eletkor"])
lista.append(szotar)
lista.append(szotar)


szotar2 = {
    "nev": "Franciska Juliska",
    "anyja_neve": "Kiss Kata",
    "Szuletesi_datum": "1972.06.26",
    "eletkor": 18,
    "jegyek": [5, 5, 5, 5, 2, 5]
    }
print(szotar["eletkor"])
lista.append(szotar)
lista.append(szotar2)
print(lista[1]["jegyek"])
print("\n")

for elem in lista:
    print(elem["nev"])


jegyek = [1, 1, 1, 1, 2, 2, 5]


def atlag(lista):
    ossz = sum(lista)
    elosztas = ossz / len(lista)
    return round(elosztas, 2)


meghivo = atlag(jegyek)
print(meghivo)
