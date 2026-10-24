# Northwind – gyakorló feladatsor 2

Ez a gyakorló feladatsor a Northwind adatbázisra épül, és a dolgozatokban szereplő SQL-témaköröket gyakoroltatja.

## Általános tudnivalók

- A feladatokat SQL-lekérdezésekkel oldd meg!
- A Northwind adatbázist és MySQL-szintaxist használd.
- Ügyelj a táblanevek és oszlopnevek pontos megadására.
- A Northwind adatbázis letöltése: https://github.com/loczylevi/adatbazis_1



## 1. feladat – Termékek szűrése

A `products` táblából jelenítsd meg a termék nevét (`product_name`) és listaárát (`list_price`), amelyek listaára nagyobb mint 15, nincsenek kivonva a forgalomból (`discontinued = 0`), és kategóriájuk nem `Condiments`. Rendezd az eredményt listaár szerint növekvő sorrendbe.

## 2. feladat – Alkalmazottak rendezése

Az `employees` táblából jelenítsd meg az alkalmazottak vezetéknevét (`last_name`), keresztnevét (`first_name`) és munkakörét (`job_title`). Rendezd az eredményt először munkakör szerint növekvő, majd vezetéknév szerint csökkenő sorrendbe.

## 3. feladat – Árakkal kapcsolatos számítások

A `products` tábla `list_price` oszlopa alapján készíts négy külön lekérdezést:

- **A)** Jelenítsd meg a legdrágább termék nevét és listaárát!
- **B)** Jelenítsd meg a legolcsóbb termék nevét és listaárát!
- **C)** Számítsd ki a termékek átlagos listaárát!
- **D)** Számítsd ki a termékek listaárainak összegét!

## 4. feladat – Alkalmazottak száma munkakörönként

Az `employees` tábla alapján határozd meg, hogy az egyes munkakörökben (`job_title`) hány alkalmazott dolgozik. Jelenítsd meg a munkakört és az alkalmazottak számát. Az eredményeket munkakörönként csoportosítsd, a létszámot függvénnyel számítsd ki.

## 5. feladat – Kategóriák átlagára

A `products` tábla alapján jelenítsd meg azoknak a kategóriáknak a nevét és átlagos listaárát, amelyeknél az átlagos listaár meghaladja a 45-öt. Az eredményeket kategóriánként csoportosítsd, és csak a feltételnek megfelelő kategóriákat jelenítsd meg.

## 6. feladat – Ügyfelek és alkalmazottak közös listája

Készíts egy lekérdezést, amely a `customers` és az `employees` táblában szereplő személyek keresztnevét (`first_name`), vezetéknevét (`last_name`) és városát (`city`) egy közös listában jeleníti meg. A két lekérdezés eredményét a `UNION` operátorral egyesítsd.

## 7. feladat – Adatbázis és táblák létrehozása

Hozz létre egy `konyvtar` nevű adatbázist! Ha már létezik ilyen nevű adatbázis, először töröld, majd hozd létre újra.

Hozd létre a `konyvek` és a `kolcsonzesek` táblákat az alábbi feltételekkel.

**A `konyvek` tábla:**
- `konyv_id`: automatikusan növekvő, egész típusú mező, elsődleges kulcs (`PRIMARY KEY`);
- `cim`: legfeljebb 100 karakter hosszú szöveges mező, kötelezően kitöltendő (`NOT NULL`);
- `ev`: egész típusú mező, alapértelmezett értéke (`DEFAULT`) 2020.

**A `kolcsonzesek` tábla:**
- `kolcsonzes_id`: automatikusan növekvő, egész típusú mező, elsődleges kulcs (`PRIMARY KEY`);
- `kolcsonzo_nev`: legfeljebb 60 karakter hosszú szöveges mező;
- `konyv_id`: egész típusú mező, idegen kulcs (`FOREIGN KEY`), amely a `konyvek` tábla `konyv_id` mezőjére hivatkozik.

A `konyvek` tábla legyen a szülőtábla, a `kolcsonzesek` tábla pedig a gyermektábla. Alakítsd ki megfelelően a kapcsolatot.

---
