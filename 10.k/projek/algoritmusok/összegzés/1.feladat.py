import random

szamok = [random.randint(1, 10) for _ in range(5)]

osszeg = sum(szamok)

print("A lista elemei:", szamok)
print("Az elemek összege:", osszeg)