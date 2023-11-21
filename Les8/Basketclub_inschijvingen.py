#%%
import datetime

naam = str(input("Wat is je naam? "))
geboorte = int(input("Wat is je geboortejaar: "))
jaar = int(datetime.date.today().strftime("%Y"))
leeftijd = jaar - geboorte
if leeftijd < 6:
    aantal_jaar = 6 - leeftijd
    print(f"{naam}, je bent nog iets te jong. Binnen {aantal_jaar} jaar ben je van harte welkom!")
else:
    if leeftijd >= 6 and leeftijd <= 8:
        ploeg = "Premicroben"
    elif leeftijd >= 9 and leeftijd <= 10:
        ploeg = "Microben"
    elif leeftijd >= 11 and leeftijd <= 12:
        ploeg = "Benjamins"
    elif leeftijd >= 13 and leeftijd <= 14:
        ploeg = "Pupillen"
    elif leeftijd >= 15 and leeftijd <= 16:
        ploeg = "Miniemen"
    elif leeftijd >= 17 and leeftijd <= 18:
        ploeg = "Cadetten"
    elif leeftijd >= 19 and leeftijd <= 21:
        ploeg = "Juniores"
    elif leeftijd >= 22:
        ploeg = "Seniores"
    print(f"{naam}, welkom bij de {ploeg}!")
# %%
