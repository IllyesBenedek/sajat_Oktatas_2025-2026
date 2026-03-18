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
    A paratlanok_szama nevű függvény,
    paraméterként egy számokat tartalmazó listát kap és
    visszatér egy számokat tartalmazó lista páros számainak számával.
    
    Üres lista esetén 0 a visszatérési érték.
'''
def paratlanok_szama(paratlanok):
    if paratlanok == []:
        return 0
    parat = 0
    for i in paratlanok:
        if i % 2 != 0:
            parat += 1
    return parat


#--------------------------
'''
    A parosok_kivalogatasa nevű függvény,
    visszatér egy listával, 
        amely a paraméterként átadott számokat tartalmazó lista
        páros számait tartalmazza.
'''
def parosok_kivalogatasa(parosok):
    par = []
    for i in parosok:
        if i % 2 == 0:
            par.append(i)
    return par


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
    A pozitivok_szama nevű függvény,
    paraméterként egy számokat tartalmazó listát kap és
    visszatér egy számokat tartalmazó lista pozitív számainak számával.
    
    Üres lista esetén 0 a visszatérési érték.
'''
def pozitivok_szama(pozitivok):
    if pozitivok == []:
        return 0
    poz = 0
    for i in pozitivok:
        if i > 0:
            poz += 1
    return poz


#--------------------------
'''
    A negativok_kivalogatasa nevű függvény,
    visszatér egy listával, 
      amely a paraméterként átadott számokat tartalmazó lista
      negatív számait tartalmazza.
'''
def negativok_kivalogatasa(negativok):
    neg = []
    for i in negativok:
        if i < 0:
            neg.append(i)
    return neg


#--------------------------
''' 
    A legnagyobb  nevű függvény,
    paraméterként egy számokat tartalmazó listát kap és
    visszatér a lista legnagyobb számával.
    Üres lista esetén None a visszatérési érték.

    A feladat megoldása során nem használhatod a max függvényt!
'''
def legnagyobb(lista):
    if lista == []:
        return None
    max = lista[0]
    for i in lista:
        if i > max:
            max = i
    return max


#--------------------------
'''
    A faktorialis nevű függvény,
    visszatér a paraméterként megkapott szám faktoriálisával.
'''
def faktorialis(n):
    if n < 0:
        return None
    faktorialis = 1
    for i in range(1, n + 1):
        faktorialis *= i
    return faktorialis


#--------------------------
'''
    A benne_van_a_listaban nevű függvény,
    első paraméterként egy listát kap,
    második paraméterként egy számot.
    A visszatérési érték True, ha  a szám benne van a listában.
    A visszatérési érték False, ha  a szám nics benne a listában.
    
    Üres lista esetén a visszatérési érték False.
'''
def benne_van_a_listaban(lista, szam):
    for i in lista:
        if i == szam:
            return True
    return False


#--------------------------
''' 
    A szorzat  nevű függvény,
    paraméterként egy számokat tartalmazó listát kap és
    visszatér a lista számainak szorzatával.
    
    Üres lista esetén 1 a visszatérési érték.
'''
def szorzat(lista):
    szam = 1
    for i in lista:
        szam *= i
    return szam


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
    if negativok == []:
        return 0
    neg = 0
    for i in negativok:
        if i < 0:
            neg += 1
    return neg


#--------------------------
'''
    A kereses_a_stringben nevű függvény,
    első paraméterként egy sztringet kap,
    második paraméterként egy betüt.
    Visszatérési érték a paraméterként megadott betü
        első előfordulási helye a stringben. 
    
    A visszatérési érték None, ha a betü nics benne a stringben.
'''
def kereses_a_stringben(string, betu):
    index = 0
    for i in string:
        if i == betu:
            return index
        index += 1
    return None



#--------------------------
''' 
    Az osszeg  nevű függvény,
    paraméterként egy számokat tartalmazó listát kap és
    visszatér a lista számainak összegével.
    Üres lista esetén 0 a visszatérési érték.
    A feladat megoldása során nem használhatod a sum() függvényt!
'''
def osszeg(lista):
    szam = 0
    for i in lista:
        szam += i
    return szam


#--------------------------
'''
    A kereses_a_listaban nevű függvény.
    Első bemeneti paraméter egy lista,
    második bemeneti paraméter egy szám.
    A visszatérési érték a paraméterként megadott szám
        első előfordulási helye a listában.
    
    A visszatérési érték None, ha a szám nics benne a listában.
'''
def kereses_a_listaban(lista, szam):
    index = 0
    for i in lista:
        if i == szam:
            return index
        index += 1
    return None


#--------------------------
''' 
    Az utolso_karakter nevű függvény,
    paraméterként egy stringet kap és
    visszatér az adott string utolso karakterével.
    
    Üres string esetén None a visszatérési érték.
'''
def utolso_karakter(string):
    if string == "":
        return None
    return string[-1]


#--------------------------
''' 
    A pozitivok_kivalogatasa nevű függvény,
    visszatér egy listával, 
        amely a paraméterként átadott számokat tartalmazó lista
        pozitiv számait tartalmazza. 
'''
def pozitivok_kivalogatasa(pozitivok):
    poz = []
    for i in pozitivok:
        if i > 0:
            poz.append(i)
    return poz


#--------------------------
''' 
    A parosok_szama  nevű függvény,
    visszatér egy számokat tartalmazó lista páros számainak számával.
    
    Üres lista esetén 0 a visszatérési érték.
'''
def parosok_szama(parosok):
    if parosok == []:
        return 0
    par = 0
    for i in parosok:
        if i % 2 == 0:
            par += 1
    return par


#======================================================================================================================C:\Users\bened\Downloads\sajat_Oktatas_2025-2026-main\sajat_Oktatas_2025-2026-main\10.k\programozas\python\python2-gyak\python2-main (2)\python2-main