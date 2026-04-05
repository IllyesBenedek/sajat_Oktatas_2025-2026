lista = ["alma", "Traktor", "teve", "béka", "Tányér", "cica", "tök", "dinnye"]
t_szavak = []
print("'t' és 'T' betüvel kezdődő szavak:")
for szo in lista:
    if szo[0].lower() == "t":
        t_szavak.append(szo)
        print(szo)

print(f"\n' listában tárolt 't/T' szaval: {t_szavak}")
