szam = int(input("adj metg egy egész számot 5 és 10 között!"))
hibak = 0

while not 5 <= szam <= 10:
    hibak += 1
    szam = int(input("helytelen érték! adj meg egy számot 5 és 10 között!"))

print("rendben")
if hibak > 0:
    print(f"Összesen {hibak} alkalommal rontottad el.")
