# forrasfajl = open("adatbeolvasas/szamozott_sorok.txt")

# forrasfajl.close()
with open("szamozott_sorok.txt", "r", encoding="UTF-8") as forrasfajl:
    print(forrasfajl.tell())
    print(forrasfajl.readline())
    forrasfajl.seek(0)
    print(forrasfajl.tell())
    print(forrasfajl.readline())
    print(forrasfajl.tell())
