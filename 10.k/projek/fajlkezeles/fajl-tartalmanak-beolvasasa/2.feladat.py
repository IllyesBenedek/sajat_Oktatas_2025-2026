with open("parduc.txt", "r", encoding="UTF-8") as versfajl:
    vers_szovege = versfajl.read()

    betuk_szama = 0
    mag_szama = 0
    maganhangzok = "aeiouáéíóöőúüűAEIOUÁÉÍÓÖŐÚÜŰ"

    # Egyetlen ciklusban megszámolunk mindent
    for karakter in vers_szovege:
        if karakter.isalpha():
            betuk_szama += 1
        if karakter in maganhangzok:
            mag_szama += 1

    szavak_szama = len(vers_szovege.split())

    print("--- A vers statisztikája ---")
    print(f"Betűk száma: {betuk_szama}")
    print(f"Magánhangzók száma: {mag_szama}")
    print(f"Szavak száma: {szavak_szama}")
