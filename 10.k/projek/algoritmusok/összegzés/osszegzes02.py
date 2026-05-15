print('Ez a program kiszámolja az átlagodat')
print('Ha már nem akarsz több jegyet megadni, írj 0-át!')
print('----------------------------------------')

darab = 0
ossszg = 0

erdemjegy = int(input("Add meg az első jegyet!"))
while erdemjegy != 0:
    darab += 1
    ossszg += erdemjegy
    erdemjegy = int(input("Add meg a következő jegyet!"))
    
if darab != 0:
    print("A megadott jegyek átlaga:", ossszg / darab)
else:
    print("Nem adtál meg érdemjegyet!")