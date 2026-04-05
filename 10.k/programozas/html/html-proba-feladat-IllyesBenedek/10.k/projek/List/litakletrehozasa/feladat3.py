import random

negyel_oszthato = []
for i in range(10):
    szam = random.randint(0, 50)
    if szam % 4 == 0:
        negyel_oszthato.append(szam)

print(f"4-gyel oszthatók: {negyel_oszthato}")
print(f"Darabszám: {len(negyel_oszthato)}")
