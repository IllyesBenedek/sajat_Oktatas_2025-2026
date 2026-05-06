import random

szamok = []

for _ in range(5):
    szamok.append(random.randint(1, 7))
    
keresett = int(input("Adj meg egy számot és megmondom benne van e a listában:"))

talalat = False
index = 0

while index < len(szamok) and not talalat:
    if szamok [index] == keresett:
        talalat = True
    index += 1

if talalat:
    print("A szám szerepel a listában.")
else:
    print("A szám nem szerepel a listában.")