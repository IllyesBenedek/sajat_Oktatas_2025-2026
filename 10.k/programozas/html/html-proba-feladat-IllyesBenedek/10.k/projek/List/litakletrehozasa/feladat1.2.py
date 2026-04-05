nevek = []
print("Nevek (ENTER=stop, max 3):")
while len(nevek) < 3:
    nev = input(f"{len(nevek)+1}.név:")
    if nev == "":
        break
    nevek.append(nev)
    if len(nevek) == 3:
        print("Max 3 név! stop.")
print("Megadott nevek:")
for nev in nevek:
    print(f"-{nev}")
