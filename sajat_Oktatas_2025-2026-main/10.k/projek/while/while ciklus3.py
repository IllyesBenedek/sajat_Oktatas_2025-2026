folytatja = True
while folytatja:
    print("vidd ki a szemetet!")
    valasz = input("mondjam még egyszer? (i/n)")
    if valasz == "n":
        folytatja = False
print("program vége!")
