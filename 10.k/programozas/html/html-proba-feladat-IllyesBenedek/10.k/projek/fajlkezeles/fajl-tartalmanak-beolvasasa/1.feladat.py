adatok = []

with open("nyelvek.txt", "r", encoding="UTF-8") as forrasfajl:

    forrasfajl.readline()

    for sor in forrasfajl:
        sor = sor.strip()
        if ";" in sor:
            reszek = sor.split(";")

            if reszek[0].isdigit():
                nyelv = {
                    "ev": int(reszek[0]),
                    "nev": reszek[1],
                    "teljes_nev": reszek[2].strip() + " " + reszek[3].strip(),
                }
                adatok.append(nyelv)

print(adatok)
