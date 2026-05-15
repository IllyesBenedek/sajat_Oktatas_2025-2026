import random

oszlopok = ["A", "B", "C"]
sorok = ["1", "2", "3"]

hajo = random.choice(oszlopok) + random.choice(sorok)

talalat = False
proba = 0

print("Torpedó játék indul!")
print("A pálya: A1 - C3")
print("Találd ki a hajó helyét!\n")

tipp = input("Add meg a tipped (pl. B2): ")

while tipp != "" and not talalat:

    proba += 1

    if tipp == hajo:
        talalat = True
        print("🎯 Talált! Elsüllyesztetted a hajót!")
    else:
        print("❌ Nem talált.")
        tipp = input("Próbáld újra (ENTER = kilépés): ")

if talalat:
    print("\nGratulálok!")
    print("Próbálkozások száma:", proba)
else:
    print("\nKiléptél a játékból.")
    print("A hajó helye ez volt:", hajo)