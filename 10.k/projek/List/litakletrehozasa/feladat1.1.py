nevek = []

print("Adjon meg neveket (ENTER-re kilép):")
while True:
    nev = input("Add meg a következő neveket:")
    if nev == "":
        print("Névbekérés vége!")
        break
    nevek.append(nev)
print("\nMegadott nevek:")
for nev in nevek:
    print(nev)
