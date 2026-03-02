import random

darab = 0

for i in range(20):
    szam = random.randint(1, 12)
    if szam % 3 == 0:
        print(szam)
        darab += 1

print("---")
print("Talált számok mennyisége:", darab)
