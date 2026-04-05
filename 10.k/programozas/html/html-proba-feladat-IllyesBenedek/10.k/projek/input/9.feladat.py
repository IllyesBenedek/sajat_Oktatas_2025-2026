fogyasztas = float(input("Autó fogyasztás (l/100km): "))
ar = float(input("Benzin ára (Ft/l): "))
tavolsag = float(input("Út hossza (km): "))
koltseg = (tavolsag / 100) * fogyasztas * ar
print("Az utazás költsége: ", koltseg, "Ft")
