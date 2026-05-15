lista = []

szo = input("Adj meg egy szót (ENTER = kilépés): ")

while szo != "":
    lista.append(szo)
    szo = input("Adj meg egy szót (ENTER = kilépés): ")

print("Lista elemei:", lista)

leghosszabb = lista[0]
legrovidebb = lista[0]

for szo in lista:
    if len(szo) < len(legrovidebb):
        legrovidebb = szo
    if len(szo) > len(leghosszabb):
        leghosszabb = szo

print("Legrövidebb szó:", legrovidebb)
print("Leghosszabb szó:", leghosszabb)