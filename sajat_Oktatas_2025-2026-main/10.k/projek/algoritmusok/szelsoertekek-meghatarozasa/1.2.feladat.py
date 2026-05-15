lista = []

szam = input("Adj meg egy számot (X = kilépés): ")

while szam.lower() != "x":
    lista.append(int(szam))
    szam = input("Adj meg egy számot (X = kilépés): ")

print("Lista elemei:", lista)

legkisebb = min(lista)
legnagyobb = max(lista)

print("Legkisebb szám:", legkisebb)
print("Legnagyobb szám:", legnagyobb)