# forrasfajl = open("adatbeolvasas/szamozott_sorok.txt")

# forrasfajl.close()

with open("szamozott_sorok.txt", "r", encoding="UTF-8") as forrasfajl:
    for sor in forrasfajl:
        print(sor.strip())
