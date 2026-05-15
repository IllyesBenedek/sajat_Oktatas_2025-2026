szo = "python"

betu = input("Adj meg egy betűt (ENTER = kilépés): ")

jo_tippek = []
rossz_tippek = []

while betu != "":

    talalat = False
    index = 0

    while index < len(szo) and not talalat:
        if szo[index] == betu:
            talalat = True
        index += 1

    if talalat:
        print("A betű előfordul a szóban.")
        jo_tippek.append(betu)
    else:
        print("A betű nem fordul elő a szóban.")
        rossz_tippek.append(betu)

    print("A szó:", szo)
    print()

    betu = input("Adj meg egy betűt (ENTER = kilépés): ")

print("\nA szó:", szo)
print("Jó tippek:", jo_tippek)
print("Rossz tippek:", rossz_tippek)