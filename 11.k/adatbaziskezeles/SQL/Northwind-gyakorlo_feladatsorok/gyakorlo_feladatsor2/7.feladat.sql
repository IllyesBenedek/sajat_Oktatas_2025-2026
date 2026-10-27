DROP DATABASE IF EXISTS konyvtar;
CREATE DATABASE konyvtar;
USE konyvtar;

CREATE TABLE konyvek (
    konyv_id INT AUTO_INCREMENT,
    cim VARCHAR(100) NOT NULL,
    ev INT DEFAULT 2020,
    PRIMARY KEY(konyv_id)
);

CREATE TABLE kolcsonzesek (
    kolcsonzes_id INT AUTO_INCREMENT,
    kolcsonzo_nev VARCHAR(60),
    konyv_id INT,
    PRIMARY KEY(kolcsonzes_id),
    FOREIGN KEY(konyv_id) REFERENCES konyvek(konyv_id)
);