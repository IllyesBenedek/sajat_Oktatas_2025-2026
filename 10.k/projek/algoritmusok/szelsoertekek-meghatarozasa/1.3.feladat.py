lista = []

szam = input("Adj meg egy számot (X = kilépés): ")

while szam.lower() != "x":
    lista.append(int(szam))
    szam = input("Adj meg egy számot (X = kilépés): ")

parosok = []

for szam in lista:
    if szam % 2 == 0:
        parosok.append(szam)

print("Lista elemei:", lista)

if len(parosok) > 0:
    print("Páros számok:", parosok)
    print("Legkisebb páros:", min(parosok))
    print("Legnagyobb páros:", max(parosok))
else:
    print("Nincs páros szám a listában.")