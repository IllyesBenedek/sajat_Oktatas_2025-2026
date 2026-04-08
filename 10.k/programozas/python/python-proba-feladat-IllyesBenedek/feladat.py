#--------------------------
''' 
    Az osszeg  nevű függvény,
    paraméterként egy számokat tartalmazó listát kap és
    visszatér a lista számainak összegével.
    Üres lista esetén 0 a visszatérési érték.
    A feladat megoldása során nem használhatod a sum() függvényt!
'''
def osszeg(lista):
    ossz = 0
    for i in lista:
        ossz += i
    return ossz

#--------------------------
'''
Feladat: Hárommal osztható számok a szövegfájlban.
Írj egy függvényt harommal_oszthato_szamok_a_fajlban néven, amely visszatér a szövegfájlban levő hárommal osztható számok listájával.
A függvény bemenő paramétere a fájl neve.
'''
def harommal_oszthato_szamok_a_fajlban(fajlnev):
    with open(fajlnev, "r") as f:
        szamok = f.read().split()
    szam = []
    for i in szamok:
        if int(i) % 3 == 0:
            szam.append(int(i))
    return szam


#--------------------------
'''
A nagyobb nevű függvény,
két számot kap és 
visszatér a nagyobb számmal.

Nem használhatod a max nevű függvényt.
'''
def nagyobb(szam1, szam2):
    if szam1 > szam2:
        return szam1
    else:
        return szam2

#--------------------------
''' 
    A negativok_szama nevű függvény,
    paraméterként egy számokat tartalmazó listát kap és
    visszatér egy számokat tartalmazó lista negativ számainak számával.
    
    Üres lista esetén 0 a visszatérési érték.
'''
def negativok_szama(negativok):
    neg = 0
    for i in negativok:
        if i < 0:
            neg += 1
    return neg


#--------------------------
'''
Feladat: String fájlba írása
A string_fajlba nevű függvény az első paraméterként kapott sztringet fájlba írja.
A fájl nevét második paraméterként kapja meg a függvény.
'''
def string_fajlba(string, fajnev):
    with open(fajnev, "w") as f:
        f.write(string)


#--------------------------
'''
A sorok_szama nevű függvény
paraméterként egy fájlnevet kap és
visszatér a fájlban levő sorok számával.
'''
def sorok_szama(fajnev):
    with open(fajnev, "r") as f:
        db = 0
        for i in f:
            db += 1
        return db


#--------------------------
'''
A karakterek_szama nevű függvény
paraméterként egy fájlnevet kap és
visszatér a fájlban levő karakterek számával. 
('\n karakterekkel együtt')
'''
def karakterek_szama(fajnev):
    with open(fajnev, "r") as f:
        karakterek = f.read()
        db = 0
        for i in karakterek:
            db += 1
        return db


#--------------------------
''' 
    A lista_atlag nevű függvény,
    paraméterként egy számokat tartalmazó listát kap és
    visszatér a lista számainak átlagával.
'''
def lista_atlag(lista):
    if lista == []:
        return 0
    atlag = 0
    for i in lista:
        atlag += i
    return atlag / len(lista)
        


#--------------------------
'''
A szavak_szama nevű függvény
paraméterként egy fájlnevet kap és
visszatér a fájlban levő szavak számával.
'''
def szavak_szama(fajnev):
    with open(fajnev, "r") as f:
        szavak = f.read().split()
    db = 0
    for i in szavak:
        db += 1
    return db
    


#--------------------------
''' 
    A legkisebb nevű függvény,
    paraméterként egy számokat tartalmazó listát kap és
    visszatér a lista legkisebb számával.
    Üres lista esetén None a visszatérési érték.
    
    A feladat megoldása során nem használhatod a min() függvényt!
'''
def legkisebb(lista):
    if lista == []:
        return None
    min = lista[0]
    for i in lista:
        if i < min:
            min = i
    return min

#--------------------------
'''
    A paratlanok_kivalogatasa nevű függvény,
    visszatér egy listával, 
        amely a paraméterként átadott számokat tartalmazó lista
        páratlan számait tartalmazza.
'''



#--------------------------
'''
Az osszead nevű nevű függvény,
két számot kap és 
visszatér a két szám összegével.

Nem használhatod a sum nevű függvényt!
'''


#--------------------------
'''
Feladat: Első karakter a szövegfájlban
Írj egy függvényt elso_karakter_a_fajlban néven, amely visszatér egy szövegfájl első karakterével.
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
Feladat: Legkisebb szám egy szövegfájlban.
Írj egy függvényt legkisebb_szam_a_fajlban néven, amely visszatér egy szövegfájlban levő lekisebb számmal.
A függvény bemenő paramétere a fájl neve.
'''




#--------------------------
'''
A kor_terulete nevű függvény, 
bemenő paraméterként kapja a kör sugarát és 
visszatér a kör területével.
'''



#--------------------------
''' 
    Az elso_karakter nevű függvény,
    paraméterként egy stringet kap és
    visszatér a string első karakterével.
    
    Üres string esetén None a visszatérési érték.
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
    A benne_van_a_stringben nevű függvény.
    első paraméterként egy stringet kap,
    második paraméterként egy betüt.
    Visszatérési értéke True, ha  a betü benne van a stringben.
    A visszatérési érték False, ha  a betü nics benne a stringben.
'''


#--------------------------
'''
A kettovel_oszthato nevű függvény, 
egy számot kap bemenetként és 
visszatér True-val, ha a szám kettővel osztható és 
visszatér False-al ha a szám kettővel nem ossztható.
'''


#======================================================================================================================/home/tanulok/illben9646/Dokumentumok/python-proba-feladat-IllyesBenedek-main