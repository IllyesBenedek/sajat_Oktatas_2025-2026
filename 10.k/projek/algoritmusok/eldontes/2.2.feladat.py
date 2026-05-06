szo = "program"

betu = input("Adj meg egy betüt:")

talalat = False
index = 0

while index < len(szo) and not talalat:
    if szo[index] == betu:
        talalat = True
    index += 1
    
if talalat:
    print("A betű előfordul a szóban.")
else:
    print("A betü nem fordul elő a szóban.")
    
print("A szó:", szo)