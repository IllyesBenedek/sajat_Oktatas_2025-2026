lista = [8, 6, 12, 17, 3, 9, 15, 24, 31, 42]

print("3-mal osztható páros számok:")
for szam in lista:
    if szam % 3 == 0 and szam % 2 == 0:
        print(szam)
