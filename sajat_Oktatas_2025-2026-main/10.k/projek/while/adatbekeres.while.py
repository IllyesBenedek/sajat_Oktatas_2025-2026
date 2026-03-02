szam = int(input("adj metg egy egész számot 5 és 10 között!"))

# while szam < 5 or 10 < szam:
while not 5 <= szam <= 10:
    szam = int(input("helytelen érték! adj meg egy számot 5 és 10 között!"))

print("rendben")
