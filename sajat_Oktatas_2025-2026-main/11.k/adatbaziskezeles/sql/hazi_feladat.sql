CREATE TABLE kedvenc_konyvek (
    id     INT  PRIMARY KEY,
    name   TEXT,
    rating INT 
);

INSERT  INTO kedvenc_konyvek
VALUES (1, "Marco Rossi", 5);

INSERT  INTO kedvenc_konyvek
VALUES (2, "Barcelona", 5);

INSERT  INTO kedvenc_konyvek
VALUES (3, "Az Aranycsapat története", 5);

INSERT  INTO kedvenc_konyvek
VALUES (4, "A futball története", 4);

INSERT  INTO kedvenc_konyvek
VALUES (5, "A futball taktikai evolúciója", 4);

SELECT *
FROM   kedvenc_konyvek;
