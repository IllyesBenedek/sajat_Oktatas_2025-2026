fajl = []
with open("nyelvek.txt", "r", encoding="UTF-8") as adatfajl:
    with open("nyelvek_masolata.txt", "w", encoding="UTF-8") as celfajl:
        adatfajl.readline()

        for sor in adatfajl:
            rezsek = sor.strip().split(";")

            szurt_adat = {
                "ev": rezsek[0],
                "nyelv": rezsek[1].strip(),
            }

            celfajl.write(f"{szurt_adat['nyelv']};{szurt_adat['ev']}\n")
print("Kész a másollat")
