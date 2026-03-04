suly = float(input("Tömeg (kg): "))
magassag_cm = float(input("Magasság (cm): "))
magassag_m = magassag_cm / 100
tti = suly / (magassag_m ** 2)
print("A testtömegindexed: ", tti)
