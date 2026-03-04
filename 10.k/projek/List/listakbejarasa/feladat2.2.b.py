lista = ["alma", "Traktor", "teve", "béka", "Tányér", "cica", "tök", "dinnye"]

megvelelo_szavak = []

for szo in lista:
    if szo[0].lower() == "t":
        megvelelo_szavak.append(szo)

print("A feltételnek megvelelő szavak listája:")
print(megvelelo_szavak)
