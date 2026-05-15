# forrasfajl = open("adatbeolvasas/szamozott_sorok.txt")

# forrasfajl.close()

with open("szamozott_sorok.txt") as forrasfajl:
    print(forrasfajl.name, forrasfajl.mode)
