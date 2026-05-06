szoveg = input("Adj meg egy szöveget: ").lower()

maganhangzok = ["a", "e", "i", "o", "u"]

for mh in maganhangzok:

    indexek = []
    i = 0

    while i < len(szoveg):
        if szoveg[i] == mh:
            indexek.append(i + 1)  # 1-től számozás
        i += 1

    if len(indexek) > 0:
        print(f"'{mh}' volt a szövegben.")
        print("Darabszám:", len(indexek))
        print("Helyek:", indexek)
    else:
        print(f"'{mh}' nem volt a szövegben.")

    print()