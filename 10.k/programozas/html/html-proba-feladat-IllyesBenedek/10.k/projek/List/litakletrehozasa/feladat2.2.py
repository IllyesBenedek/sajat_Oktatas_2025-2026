szavak = []
print("'a/A' betüvel kezdödő szavak (ENTER=stop):")

while True:
    szo = input()
    if szo == "":
        break
    if szo[0].lower() == "a":
        szavak.append(szo)

print("'a/A' betüvel kezdődő szavak:", szavak)
