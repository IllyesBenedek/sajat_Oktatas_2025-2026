lista = []

szam = input("Adj meg egy számot (ENTER = kilépés): ")

while szam != "":
    lista.append(int(szam))
    szam = input("Adj meg egy számot (ENTER = kilépés): ")

legkisebb = min(lista)
legnagyobb = max(lista)

print("Lista:", lista)
print("Legkisebb:", legkisebb)
print("Legnagyobb:", legnagyobb)