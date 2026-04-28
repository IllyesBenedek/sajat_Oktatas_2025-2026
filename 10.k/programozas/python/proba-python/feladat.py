#--------------------------
'''
Feladat: Hárommal osztható számok a szövegfájlban.
Írj egy függvényt harommal_oszthato_szamok_a_fajlban néven, amely visszatér a szövegfájlban levő hárommal osztható számok listájával.
A függvény bemenő paramétere a fájl neve.
'''
def harommal_oszthato_szamok_a_fajlban(fajnev):
    with open(fajnev, "r") as f:
        szam = f.read().split()
    harom = []
    for i in szam:
        if int(i) % 3 == 0:
            harom.append(int(i))
    return harom

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
A karakterek_szama nevű függvény
paraméterként egy fájlnevet kap és
visszatér a fájlban levő karakterek számával. 
('\n karakterekkel együtt')
'''
def karakterek_szama(fajnev):
    with open(fajnev, "r") as f:
        karakter = f.read()
    return len(karakter)        


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
    
    def felszin(self):
        return 6 * self.a **2
    
    def terfogat(self):
        return self.a ** 3


#--------------------------
'''
A sorok_szama nevű függvény
paraméterként egy fájlnevet kap és
visszatér a fájlban levő sorok számával.
'''
def sorok_szama(fajnev):
    with open(fajnev, "r") as f:
        sorok = f.readlines()
    return len(sorok)


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
    Az elso_karakter nevű függvény,
    paraméterként egy stringet kap és
    visszatér a string első karakterével.
    
    Üres string esetén None a visszatérési érték.
'''
def elso_karakter(string):
    if string == "":
        return None
    return string[0]


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
Feladat: String fájlba írása
A string_fajlba nevű függvény az első paraméterként kapott sztringet fájlba írja.
A fájl nevét második paraméterként kapja meg a függvény.
'''
def string_fajlba(string, fajnev):
    with open(fajnev, "w") as f:
     f.write(string)   


#--------------------------
'''
Az osszead nevű nevű függvény,
két számot kap és 
visszatér a két szám összegével.

Nem használhatod a sum nevű függvényt!
'''
def osszead(szam1, szan2):
    return szam1 + szan2


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
class Teglalap:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        
    def kerulet(self):
        return 2 * self.a + 2 * self.b

    def terulet(self):
        return self.a * self.b


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
A kor_terulete nevű függvény, 
bemenő paraméterként kapja a kör sugarát és 
visszatér a kör területével.
'''
import math
def kor_terulete(r):
    return r ** 2 * math.pi


#--------------------------
'''
Feladat: Első karakter a szövegfájlban
Írj egy függvényt elso_karakter_a_fajlban néven, amely visszatér egy szövegfájl első karakterével.
A függvény bemenő paramétere a fájl neve.
'''
def elso_karakter_a_fajlban(fajnev):
    with open(fajnev, "r") as f:
        karaakter = f.read(1)
    return karaakter


#--------------------------
'''
A szavak_szama nevű függvény
paraméterként egy fájlnevet kap és
visszatér a fájlban levő szavak számával.
'''
def szavak_szama(fajnev):
    with open(fajnev, "r") as f:
        szo = f.read().split()
    return len(szo)


#======================================================================================================================C:\beni\Informatika\10.k\Programozás\proba-python