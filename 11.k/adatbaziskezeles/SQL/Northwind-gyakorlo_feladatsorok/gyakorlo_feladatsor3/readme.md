# Northwind – gyakorló feladatsor 3

Ez a gyakorló feladatsor a Northwind adatbázisra épül, és a dolgozatokban szereplő SQL-témaköröket gyakoroltatja.

## Általános tudnivalók

- A feladatokat SQL-lekérdezésekkel oldd meg!
- A Northwind adatbázist és MySQL-szintaxist használd.
- Ügyelj a táblanevek és oszlopnevek pontos megadására.
- A Northwind adatbázis letöltése: https://github.com/loczylevi/adatbazis_1


## 1. feladat – Termékek szűrése

A `products` táblából jelenítsd meg a termék nevét (`product_name`) és listaárát (`list_price`), amelyek listaára kisebb mint 60, nincsenek kivonva a forgalomból (`discontinued = 0`), és kategóriájuk nem `Beverages`. Rendezd az eredményt listaár szerint csökkenő sorrendbe.

## 2. feladat – Alkalmazottak rendezése

Az `employees` táblából jelenítsd meg az alkalmazottak keresztnevét (`first_name`), vezetéknevét (`last_name`) és munkakörét (`job_title`). Rendezd az eredményt először vezetéknév szerint növekvő, majd keresztnév szerint csökkenő sorrendbe.

## 3. feladat – Árakkal kapcsolatos számítások

A `products` tábla `list_price` oszlopa alapján készíts négy külön lekérdezést:

- **A)** Jelenítsd meg a legolcsóbb termék nevét és listaárát!
- **B)** Jelenítsd meg a legdrágább termék nevét és listaárát!
- **C)** Számítsd ki a termékek átlagos listaárát!
- **D)** Számítsd ki a termékek listaárainak összegét!

## 4. feladat – Rendelések száma országonként

Az `orders` tábla alapján határozd meg, hogy az egyes szállítási országokból (`ship_country`) hány rendelés szerepel az adatbázisban. Jelenítsd meg a szállítási országot és a rendelések számát. Az eredményeket országonként csoportosítsd.

## 5. feladat – Kategóriák átlagára

A `products` tábla alapján jelenítsd meg azoknak a kategóriáknak a nevét és átlagos listaárát, amelyeknél az átlagos listaár meghaladja a 35-öt. Az eredményeket kategóriánként csoportosítsd, és csak a feltételnek megfelelő kategóriákat jelenítsd meg.

## 6. feladat – Ügyfelek és alkalmazottak közös listája

Készíts egy lekérdezést, amely a `customers` és az `employees` táblában szereplő személyek keresztnevét (`first_name`), vezetéknevét (`last_name`) és városát (`city`) egy közös listában jeleníti meg. A két lekérdezés eredményét a `UNION` operátorral egyesítsd.

## 7. feladat – Adatbázis és táblák létrehozása

Hozz létre egy `etterem` nevű adatbázist! Ha már létezik ilyen nevű adatbázis, először töröld, majd hozd létre újra.

Hozd létre az `etelek` és a `rendelesek` táblákat az alábbi feltételekkel.

**Az `etelek` tábla:**
- `etel_id`: automatikusan növekvő, egész típusú mező, elsődleges kulcs (`PRIMARY KEY`);
- `etel_nev`: legfeljebb 80 karakter hosszú szöveges mező, kötelezően kitöltendő (`NOT NULL`);
- `ar`: egész típusú mező, alapértelmezett értéke (`DEFAULT`) 1500.

**A `rendelesek` tábla:**
- `rendeles_id`: automatikusan növekvő, egész típusú mező, elsődleges kulcs (`PRIMARY KEY`);
- `vendeg_nev`: legfeljebb 60 karakter hosszú szöveges mező;
- `etel_id`: egész típusú mező, idegen kulcs (`FOREIGN KEY`), amely az `etelek` tábla `etel_id` mezőjére hivatkozik.

Az `etelek` tábla legyen a szülőtábla, a `rendelesek` tábla pedig a gyermektábla. Alakítsd ki megfelelően a kapcsolatot.

---

