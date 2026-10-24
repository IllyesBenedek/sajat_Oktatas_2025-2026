# Northwind – gyakorló feladatsor 1

Ez a gyakorló feladatsor a Northwind adatbázisra épül, és a dolgozatokban szereplő SQL-témaköröket gyakoroltatja.

## Általános tudnivalók

- A feladatokat SQL-lekérdezésekkel oldd meg!
- A Northwind adatbázist és MySQL-szintaxist használd.
- Ügyelj a táblanevek és oszlopnevek pontos megadására.
- A Northwind adatbázis letöltése: https://github.com/loczylevi/adatbazis_1

## 1. feladat – Termékek szűrése

A `products` táblából jelenítsd meg a termékek nevét (`product_name`) és listaárát (`list_price`), amelyek:

- listaára nagyobb mint 25;
- nincsenek kivonva a forgalomból (`discontinued = 0`);
- kategóriájuk nem `Seafood`.

Az eredményt listaár szerint **csökkenő sorrendbe** rendezd.

## 2. feladat – Alkalmazottak rendezése

Az `employees` táblából jelenítsd meg az alkalmazottak keresztnevét (`first_name`), vezetéknevét (`last_name`) és munkakörét (`job_title`).

Rendezd az eredményt először munkakör szerint növekvő, majd vezetéknév szerint csökkenő sorrendbe.

## 3. feladat – Árakkal kapcsolatos számítások

A `products` tábla `list_price` oszlopa alapján készíts **négy külön SQL-lekérdezést**:

- **A)** Jelenítsd meg a legolcsóbb termék nevét és listaárát!
- **B)** Jelenítsd meg a legdrágább termék nevét és listaárát!
- **C)** Számítsd ki a termékek átlagos listaárát!
- **D)** Számítsd ki a termékek listaárainak összegét!

## 4. feladat – Rendelések számolása

Az `orders` tábla alapján határozd meg, hogy az egyes szállítási országokból (`ship_country`) hány rendelés szerepel az adatbázisban!

Jelenítsd meg a szállítási ország nevét és a rendelések számát. Az eredményeket országonként csoportosítsd.

## 5. feladat – Kategóriák átlagára

A `products` tábla alapján jelenítsd meg azoknak a kategóriáknak a nevét és átlagos listaárát, amelyeknél az átlagos listaár **meghaladja a 40-et**.

Az eredményeket kategóriánként csoportosítsd, az átlagot függvénnyel számítsd ki, és csak a feltételnek megfelelő kategóriákat jelenítsd meg.

## 6. feladat – Közös személylista

Készíts egy lekérdezést, amely a `customers` és az `employees` táblákban szereplő személyek keresztnevét (`first_name`), vezetéknevét (`last_name`) és városát (`city`) egy közös listában jeleníti meg.

A két lekérdezés eredményét a `UNION` operátorral egyesítsd.

## 7. feladat – Adatbázis és táblák létrehozása

Hozz létre egy `mozi` nevű adatbázist! Ha már létezik ilyen nevű adatbázis, először töröld, majd hozd létre újra!

Az adatbázisban hozd létre a `termek` és a `vetitesek` táblákat az alábbi feltételekkel.

### A `termek` tábla

- `terem_id`: automatikusan növekvő, egész típusú mező, elsődleges kulcs (`PRIMARY KEY`);
- `ferohely`: egész típusú mező, alapértelmezett értéke (`DEFAULT`) 50.

### A `vetitesek` tábla

- `vetites_id`: automatikusan növekvő, egész típusú mező, elsődleges kulcs (`PRIMARY KEY`);
- `film_cim`: legfeljebb 80 karakter hosszú szöveges mező;
- `terem_id`: egész típusú mező, idegen kulcs (`FOREIGN KEY`), amely a `termek` tábla `terem_id` mezőjére hivatkozik.

A `termek` tábla legyen a **szülőtábla**, a `vetitesek` tábla pedig a **gyermektábla**! Gondoskodj a táblák közötti kapcsolat megfelelő kialakításáról.

---

