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
A karakterek_szama nevű függvény
paraméterként egy fájlnevet kap és
visszatér a fájlban levő karakterek számával. 
('\n karakterekkel együtt')
'''
def karakterek_szama(fajnev):
    with open(fajnev, "r") as f:
        karakter = f.read()
    db = 0
    for i in karakter:
        db += 1
    return db


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
Feladat: Legkisebb szám egy szövegfájlban.
Írj egy függvényt legkisebb_szam_a_fajlban néven, amely visszatér egy szövegfájlban levő lekisebb számmal.
A függvény bemenő paramétere a fájl neve.
'''
def legkisebb_szam_a_fajlban(fajnev):
    with open(fajnev, "r") as f:
        lista = f.read().split()
    if lista == []:
        return None
    min = int(lista[0])
    for i in lista:
        if int(i) < min:
            min = int(i)
    return min


#--------------------------
'''
A kettovel_oszthato nevű függvény, 
egy számot kap bemenetként és 
visszatér True-val, ha a szám kettővel osztható és 
visszatér False-al ha a szám kettővel nem ossztható.
'''
def kettovel_oszthato(szam):
    return szam % 2 == 0


#--------------------------
'''
    A benne_van_a_stringben nevű függvény.
    első paraméterként egy stringet kap,
    második paraméterként egy betüt.
    Visszatérési értéke True, ha  a betü benne van a stringben.
    A visszatérési érték False, ha  a betü nics benne a stringben.
'''
def benne_van_a_stringben(string, betu):
    for i in string:
        if i == betu:
            return True
    return False


#--------------------------
'''
Az osszead nevű nevű függvény,
két számot kap és 
visszatér a két szám összegével.

Nem használhatod a sum nevű függvényt!
'''
def osszead(szam1, szam2):
    return szam1 + szam2


#--------------------------
'''
Feladat: Első karakter a szövegfájlban
Írj egy függvényt elso_karakter_a_fajlban néven, amely visszatér egy szövegfájl első karakterével.
A függvény bemenő paramétere a fájl neve.
'''
def elso_karakter_a_fajlban(fajnev):
    with open(fajnev, "r") as f:
        karakter = f.read()
    if karakter == "":
        return None
    return karakter[0]


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
class Kocka:
    def __init__(self, a):
        self.a = a
    def terfogat(self):
        return self.a ** 3
    def felszin(self):
        return 6 * self.a * self.a
        


#--------------------------
'''
    A paratlanok_kivalogatasa nevű függvény,
    visszatér egy listával, 
        amely a paraméterként átadott számokat tartalmazó lista
        páratlan számait tartalmazza.
'''
def paratlanok_kivalogatasa(paratlanok):
    parat = []
    for i in paratlanok:
        if i % 2 != 0:
            parat.append(i)
    return parat


#--------------------------
''' 
    Az elso_karakter nevű függvény,
    paraméterként egy stringet kap és
    visszatér a string első karakterével.
    
    Üres string esetén None a visszatérési érték.
'''



#--------------------------
'''
Feladat: Hárommal osztható számok a szövegfájlban.
Írj egy függvényt harommal_oszthato_szamok_a_fajlban néven, amely visszatér a szövegfájlban levő hárommal osztható számok listájával.
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
A kor_terulete nevű függvény, 
bemenő paraméterként kapja a kör sugarát és 
visszatér a kör területével.
'''



#--------------------------
''' 
    A negativok_szama nevű függvény,
    paraméterként egy számokat tartalmazó listát kap és
    visszatér egy számokat tartalmazó lista negativ számainak számával.
    
    Üres lista esetén 0 a visszatérési érték.
'''



#--------------------------
''' 
    A legkisebb nevű függvény,
    paraméterként egy számokat tartalmazó listát kap és
    visszatér a lista legkisebb számával.
    Üres lista esetén None a visszatérési érték.
    
    A feladat megoldása során nem használhatod a min() függvényt!
'''



#--------------------------
'''
A szavak_szama nevű függvény
paraméterként egy fájlnevet kap és
visszatér a fájlban levő szavak számával.
'''



#--------------------------
'''
Feladat: String fájlba írása
A string_fajlba nevű függvény az első paraméterként kapott sztringet fájlba írja.
A fájl nevét második paraméterként kapja meg a függvény.
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
    Az osszeg  nevű függvény,
    paraméterként egy számokat tartalmazó listát kap és
    visszatér a lista számainak összegével.
    Üres lista esetén 0 a visszatérési érték.
    A feladat megoldása során nem használhatod a sum() függvényt!
'''



#======================================================================================================================C:\Users\bened\Downloads\sajat_Oktatas_2025-2026\10.k\programozas\python\proba-python