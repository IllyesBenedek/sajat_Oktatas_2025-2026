lista = ["eper", "Alma", "kutya", "Erdő", "ház", "teve", "kecske"]

darab = 0
e_szavak = []

for szo in lista:
    if "e" in szo.lower():
        darab += 1
        e_szavak.append(szo)

print("E/e betűt tartalmazó szavak:", e_szavak)
print("Darabszám:", darab)