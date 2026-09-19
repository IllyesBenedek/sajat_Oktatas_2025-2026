import os

fajl_utvonal = "szamozott_sorok.txt"

if os.path.exists(fajl_utvonal):
    with open(fajl_utvonal, "r", encoding="UTF-8") as forrasfajl:
        print("Sikerült megnyitni a fájlt!")
        print(forrasfajl.readline())
else:
    print(f"Hiba: A fájl nem található itt: {fajl_utvonal}")
