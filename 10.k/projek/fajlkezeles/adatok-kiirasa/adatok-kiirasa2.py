with open("messi.webp", "rb") as eredeti:
    with open("messi_masolat.jpg", "wb") as masolat:
        darab_meret = 4096
        darab = eredeti.read(darab_meret)

        while len(darab) > 0:
            masolat.write(darab)
            darab = eredeti.read(darab_meret)
