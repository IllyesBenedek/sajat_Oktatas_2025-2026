while True:
    mondat = input("Írj egy mondatot (kilépéshez Entert): ")
    if mondat == "":
        break
    if "." in mondat:
        print("Ez egy kijelentő mondat: ")
    if "?" in mondat:
        print("Ez egy kérdő mondat")
    if "!" in mondat:
        print("Ez egy felkiáltó /felszólító /óhajtó mondat")
