while True:
    mondat = input("Írj egy mondatot (kilépéshez Entert): ")

    if mondat == "":
        break

    if "?" in mondat:
        print("Ez egy kérdő mondat: ")

    elif "!" in mondat:
        print("Ez egy felkiáltó /felszólító /óhajtó mondat: ")

    elif "." in mondat:
        print("Ez egy kijelentő mondat: ")
    else:
        print("Ebben a mondatban nincs alapvető mondatzáró írásjel: ")
print("Program vége")
