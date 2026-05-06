lista = ["Alma", "banán", "Autó", "kutya", "asztal", "eper", "Árnyék"]

darab = 0
a_szavak = []

for szo in lista:
    if szo[0].lower() == "a":
        darab += 1
        a_szavak.append(szo)

print("A/A-val kezdődő szavak:", a_szavak)
print("Darabszám:", darab)