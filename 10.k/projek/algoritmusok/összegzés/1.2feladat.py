import random

szamok = [random.randint(1, 10) for _ in range(5)]

osszeg = 0
for szam in szamok:
    if szam % 2 == 0:
        osszeg += szam

print(f"A számok: {szamok}")
print(f"A párosok összege: {osszeg}")