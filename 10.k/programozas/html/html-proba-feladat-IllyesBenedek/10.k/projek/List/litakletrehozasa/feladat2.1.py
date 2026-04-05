a_szavak = []
print('"a"-s szavak (Enter=Stop):')

while True:
    szo = input()
    if szo == "":
        break
    if szo.lower().startswith("a"):
        a_szavak.append(szo)

print('"a"-s szavak:', a_szavak)
