with open("parduc.txt", "r", encoding="UTF-8") as versfajl:
    vers_szovege = versfajl.read()

    betuk_szama = 0
    for karakter in vers_szovege:
        if karakter.isalpha():
            betuk_szama += 1

    maganhangzok = "aeiouáéíóöőúüűAEIOUÁÉÍÓÖŐÚÜŰ"
    mag_szama = 0
    for karakter in vers_szovege:
        if karakter in maganhangzok:
            mag_szama += 1

    szavak_listája = vers_szovege.split()
    szavak_szama = len(szavak_listája)

    print("--A vers statisztikája---")
    print(f"Betűk száma: {betuk_szama}")
    print(f"Magánhangzók száma: {mag_szama}")
    print(f"Szavak száma: {szavak_szama}")
