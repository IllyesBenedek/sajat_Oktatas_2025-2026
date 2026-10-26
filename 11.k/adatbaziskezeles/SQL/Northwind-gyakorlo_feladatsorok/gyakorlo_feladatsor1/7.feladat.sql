DROP DATABASE IF EXISTS mozi;
CREATE DATABASE mozi;
USE mozi;

CREATE TABLE termek (
    terem_id INT AUTO_INCREMENT,
    ferohely INT DEFAULT 50,
    PRIMARY KEY (terem_id)
);

CREATE TABLE vetitesek (
    vetites_id INT AUTO_INCREMENT,
    film_cim VARCHAR(80),
    terem_id INT,
    PRIMARY KEY (vetites_id),
    FOREIGN KEY (terem_id) REFERENCES termek(terem_id)
);