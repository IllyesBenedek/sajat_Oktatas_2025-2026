szam = int(input("Adj meg egy páros számot: "))

while szam % 2 != 0:
    print("Ez egy páratlan szám volt. Próbáld újra!")
    szam = int(input("Adj meg egy páros számot: "))

print("Köszönöm! Végre egy páros szám.")
