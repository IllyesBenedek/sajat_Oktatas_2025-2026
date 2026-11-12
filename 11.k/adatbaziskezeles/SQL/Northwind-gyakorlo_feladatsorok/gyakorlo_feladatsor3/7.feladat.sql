DROP DATABASE IF EXISTS etterem;
CREATE DATABASE etterem;
USE etterem;

CREATE TABLE etelek(
    etel_id INT AUTO_INCREMENT,
    etel_nev VARCHAR(80) NOT NULL,
    ar INT DEFAULT(1500),
    PRIMARY KEY(etel_id)
);

CREATE TABLE rendelesek(
    rendeles_id INT AUTO_INCREMENT,
    vendeg_nev VARCHAR(60),
    etel_id INT,
    PRIMARY KEY(rendeles_id),
    FOREIGN KEY(etel_id) REFERENCES etelek(etel_id)
);