#%%
import random

def aantal_ogen(doel_aantal):
    poging = 0
    while True:
        worp = random.randint(1, 6)
        poging += 1
        print(f"Poging {poging} : {worp}")
        if worp == doel_aantal:
            break
    return f"In {poging} pogingen werd een {doel_aantal} gedobbeld"

aantal = int(input("Hoeveel ogen wil je werpen? "))
resultaat = aantal_ogen(aantal)
print(resultaat)
