# mode: r /w /a+ /x


with open("szamozott_sorok.txt", "r", encoding="UTF-8") as forrasfajl:
    with open("szamozott_sorok_masolat.txt", "x", encoding="UTF-8") as celfajl:
        for sor in forrasfajl:
            print(sor.strip(), file=celfajl)
