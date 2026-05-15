szamok = []

szam = int(input("Adj meg egy számot [-5;5] között: "))

while szam >= -5 and szam <= 5:
    szamok.append(szam)
    szam = int(input("Adj meg egy következő számot:"))
    
osszeg = sum(szamok)

print("A megadott intervallumba eső számok:", szamok)
print("A számok összege:", osszeg)