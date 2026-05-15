# forrasfajl = open("adatbeolvasas/szamozott_sorok.txt")

# forrasfajl.close()

autok = []
with open("autok_listaja.csv", "r", encoding="UTF-8") as forrasfajl:
    for sor in forrasfajl:
        adatok = sor.strip().split(",")
        auto = {
            "rendszam": adatok[0],
            "tipus": adatok[1],
            "kor": int(adatok[2])
            }
        autok.append(auto)

print(f"{autok=}")
