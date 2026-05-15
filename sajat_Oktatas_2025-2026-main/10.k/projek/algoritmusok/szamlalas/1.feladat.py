import random

lista = []

for _ in range(5):
    lista.append(random.randint(1, 10))
    
darab = 0
for szam in lista:
    if szam % 2 == 0:
        darab += 1
        
print("Lista elemei:", lista)
print("Páros számok száma:", darab)