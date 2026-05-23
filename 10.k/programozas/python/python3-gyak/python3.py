#--------------------------
'''
Feladat: Páros számok száma egy szövegfájlban.
Írj egy függvényt paros_szamok_szama_a_fajlban néven, amely visszatér egy szövegfájlban levő páros számok számával.
A függvény bemenő paramétere a fájl neve.
'''
def paros_szamok_szama_a_fajlban(fajnev):
    with open(fajnev) as f:
        szam = f.read().split()
    par = 0
    for i in szam:
        if int(i) % 2 == 0:
            par += 1
    return par


#--------------------------
'''
Feladat: Páratlan számok száma egy szövegfájlban.
Írj egy függvényt paratlan_szamok_szama_a_fajlban néven, amely visszatér egy szövegfájlban levő páratlan számok számával.
A függvény bemenő paramétere a fájl neve.
'''
def paratlan_szamok_szama_a_fajlban(fajnev):
    with open(fajnev) as f:
        szam = f.read().split()
    parat = 0
    for i in szam:
        if int(i) % 2 != 0:
            parat += 1
    return parat

#--------------------------
'''
Feladat: Párosok egy szövegfájlból.
Írj egy függvényt parosok_a_fajlbol néven, amely visszatér a szövegfájlban levő páros számokkal mint listával.
A függvény bemenő paramétere a fájl neve.
'''
def parosok_a_fajlbol(fajnev):
    with open(fajnev) as f:
        szam = f.read().split()
    par = []
    for i in szam:
        if int(i) % 2 == 0:
            par.append(int(i))
    return par


#--------------------------
'''
Feladat: Számok átlaga egy szövegfájlban.
Írj egy függvényt szamok_atlaga_a_fajlban néven, amely visszatér egy szövegfájlban levő számok átlagával.
A függvény bemenő paramétere a fájl neve.
'''
def szamok_atlaga_a_fajlban(fajnev):
    with open(fajnev) as f:
        lista = f.read().split()
    atlag = 0
    for i in lista:
        atlag += int(i)
    return atlag / len(lista)


#--------------------------
'''
A leggyakoribb_karakter(fname) függvény
paraméterként egy fájlnevet kap és
visszatér a  fájlban leggyakrabban előforduló karakterrel.
'''
def leggyakoribb_karakter(fajnev):
    with open(fajnev) as f:
        karakter = f.read()
    leggyakorib = karakter[0]
    for i in karakter:
        if karakter.count(i) > karakter.count(leggyakorib):
            leggyakorib = i
    return leggyakorib



#--------------------------
'''
A leghosszabb_sor_hossza(fname) függvény
paraméterként egy fájlnevet kap és
visszatér a  fájlban levő leghosszabb sor hosszával.
'''
def leghosszabb_sor_hossza(fajnev):
    with open(fajnev) as f:
        sorok = f.read()
    leghosszab = 0
    for i in sorok:
        if len(i) > leghosszab:
            leghosszab = len(i)
    return leghosszab


#--------------------------
'''
Feladat: String fájlba írása
A string_fajlba nevű függvény az első paraméterként kapott sztringet fájlba írja.
A fájl nevét második paraméterként kapja meg a függvény.
'''



#--------------------------
'''
Feladat: Negatív számok száma egy szövegfájlban.
Írj egy függvényt negativ_szamok_szama_a_fajlban néven, amely visszatér egy szövegfájlban levő negativ számok számával.
A függvény bemenő paramétere a fájl neve.
'''



#--------------------------
'''
Feladat: Páratlanok egy szövegfájlból.
Írj egy függvényt paratlanok_a_fajlbol néven, amely visszatér a szövegfájlban levő páratlan számokkal mint listával.
A függvény bemenő paramétere a fájl neve.
'''



#--------------------------
'''
A szavak_szama nevű függvény
paraméterként egy fájlnevet kap és
visszatér a fájlban levő szavak számával.
'''



#--------------------------
'''
Feladat: Kocka osztály definiálása. 
[Objektumorientált programozás]
Hozz létre egy osztályt Kocka néven.
A Kocka osztály lehetővé teszi a kocka oldalhosszúságának tárolását.
A Kocka osztály rendelkezik egy tefogat() nevü metódussal, 
    amely az osztály segítségével létrehozott objektum metódusaként 
        visszaadja az adott objektum térfogatát.
A Kocka osztály rendelkezik egy felszin() nevü metódussal, 
    amely az osztály segítségével létrehozott objektum metódusaként 
    visszaadja az adott objektum felszínét.
'''



#--------------------------
'''
Feladat: Számok összege egy szövegfájlban.
Írj egy függvényt szamok_osszege_a_fajlban néven amely visszatér egy szövegfájlban levő számok összegével.
A függvény bemenő paramétere a fájl neve.
'''



#--------------------------
'''
A sorok_szama nevű függvény
paraméterként egy fájlnevet kap és
visszatér a fájlban levő sorok számával.
'''



#--------------------------
'''
Feladat: Legkisebb szám egy szövegfájlban.
Írj egy függvényt legkisebb_szam_a_fajlban néven, amely visszatér egy szövegfájlban levő lekisebb számmal.
A függvény bemenő paramétere a fájl neve.
'''



#--------------------------
'''
Feladat: Utolsó karakter a szövegfájlban
Írj egy függvényt utolso_karakter_a_fajlban néven, amely visszatér egy szövegfájl utolsó karakterével.
A függvény bemenő paramétere a fájl neve.
'''



#--------------------------
'''
Feladat: Téglalap osztály definiálása. 
[Objektumorientált programozás]
Hozz létre egy osztályt Teglalap néven.
A Teglalap osztály lehetővé teszi a téglalap oldalhosszúságainak tárolását.
A Teglalap osztály rendelkezik egy kerulet() nevü metódussal, 
    amely az osztály segítségével létrehozott objektum metódusaként 
        visszaadja az adott objektum kerületét.
A Teglalap osztály rendelkezik egy terulet() nevü metódussal, 
    amely az osztály segítségével létrehozott objektum metódusaként 
        visszaadja az adott objektum területét.
'''



#--------------------------
'''
Feladat: Első karakter a szövegfájlban
Írj egy függvényt elso_karakter_a_fajlban néven, amely visszatér egy szövegfájl első karakterével.
A függvény bemenő paramétere a fájl neve.
'''



#--------------------------
'''
Feladat: Számtani sorozat fájlba írása
Készíts függvényt szaz_szam_fajlba néven, amely 1-tól 100-ig egyesével kiírja a számokat egy fájlba.
Minden szám kerüljön új sorba.
A fájl nevét paraméterként kapja meg a függvény.
'''



#--------------------------
'''
Feladat: Hárommal osztható számok a szövegfájlban.
Írj egy függvényt harommal_oszthato_szamok_a_fajlban néven, amely visszatér a szövegfájlban levő hárommal osztható számok listájával.
A függvény bemenő paramétere a fájl neve.
'''



#--------------------------
'''
A lorem_szavak_szama nevű függvény 
paraméterként egy fájlnevet kap és
visszatér a  fájlban levő "lorem" szavak számával.
'''



#--------------------------
'''
Feladat: Legnagyobb szám egy szövegfájlban.
Írj egy függvényt legnagyobb_szam_a_fajlban néven, amely visszatér egy szövegfájlban levő legnagyobb számmal.
A függvény bemenő paramétere a fájl neve.
'''



#--------------------------
'''
Feladat: Négyzet osztály definiálása. 
[Objektumorientált programozás]
Hozz létre egy osztályt Negyzet néven.
A Negyzet osztály lehetővé teszi a negyzet oldalhosszúságának tárolását.
A Negyzet osztály rendelkezik egy kerulet() nevü metódussal, 
    amely az osztály segítségével létrehozott objektum metódusaként 
        visszaadja az adott objektum kerületét.
A Negyzet osztály rendelkezik egy terulet() nevü metódussal, 
    amely az osztály segítségével létrehozott objektum metódusaként 
        visszaadja az adott objektum területét.
'''



#--------------------------
'''
Feladat: Leggyakoribb szám a szövegfájlban.
Írj egy függvényt leggyakoribb_szam_a_fajlban néven, amely visszatér a szövegfájlban levő leggyakoribb számmal.
A függvény bemenő paramétere a fájl neve.
'''



#--------------------------
'''
Feladat: Neggyel osztható számok a szövegfájlban.
A neggyel_oszthato_szamok_a_fajlban függvény
egy függvényt neggyel_oszthato_szamok_a_fajlban néven, amely visszatér a szövegfájlban levő neggyel osztható számok listájával.
A függvény bemenő paramétere a fájl neve.
'''



#--------------------------
'''
Az r_betuk_szama nevű függvény
paraméterként egy fájlnevet kap és
visszatér a fájlban levő 'r' betük számával.
'''



#--------------------------
'''
Feladat: Negatívok egy szövegfájlból.
Írj egy függvényt negativok_a_fajlbol néven, amely visszatér a szövegfájlban levő negativ számokkal mint listával.
A függvény bemenő paramétere a fájl neve.
'''



#--------------------------
'''
Feladat: Pozitív számok száma egy szövegfájlban.
Írj egy függvényt pozitiv_szamok_szama_a_fajlban néven, amely visszatér egy szövegfájlban levő pozitiv számok számával.
A függvény bemenő paramétere a fájl neve.
'''



#--------------------------
'''
Feladat: Pozitívok egy szövegfájlból.
Írj egy függvényt pozitiv_a_fajlbol néven, amely visszatér a szövegfájlban levő pozitiv számokkal mint listával.
A függvény bemenő paramétere a fájl neve.
'''



#--------------------------
'''
A karakterek_szama nevű függvény
paraméterként egy fájlnevet kap és
visszatér a fájlban levő karakterek számával. 
('\n karakterekkel együtt')
'''



#======================================================================================================================C:\Users\bened\Downloads\sajat_Oktatas_2025-2026-main\sajat_Oktatas_2025-2026-main\10.k\programozas\python\python3-main\python3-main