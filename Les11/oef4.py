import random 
class CijferSpel:
    def __init__(self, code = (0,0,0,0,0)):
        self.code = code
        if self.code == (0,0,0,0,0):
            self.code = (random.randint(0,9), random.randint(0,9), random.randint(0,9), random.randint(0,9), random.randint(0,9))

    def tel_juiste_positie(self, gok):
        antwoord = 0
        if CijferSpel.juiste_input(gok) == False:
            print("Dit is geen geldige gok")
        else:
            for i, j in self, gok:
                if i == j:
                    antwoord += 1
                return antwoord
            
    def tel_som_juiste_positie(self, gok):
        som = 0
        if CijferSpel.juiste_input(gok) != False:
            print("Dit is geen geldige gok")
        else:
            for j in gok:
                som += j
            return som
        
    def juiste_gok(self, gok):
        if self.code == gok:
            return True
        else:
            return False
        
    def juiste_input(self, gok):
        if type(gok) == tuple and len(gok) == 5:
            return True
        else:
            return False

    def __str__(self):
        return str(self.code)
    
geheime_code = CijferSpel((5,1,1,1,1))
aantal_gok = int(input("Hoeveel keer een gok wilt uitvoeren? "))
gok_over = aantal_gok
for i in range(aantal_gok):
    gok = tuple(input("Waag je gok, geef 5 cijfers, je hebt nog {gok_over} poging(en): "))
    print("Je gok was: ")
    gok_over -= 1

    if CijferSpel.juiste_gok(gok):
        print("Proficiat! Je hebt de code gekraakt in {i} beurten.")
        break
    else:
        print("Nog niet helemaal juist!")
        aantal_cijfers = CijferSpel.tel_juiste_positie(gok)
        som_cijfers = CijferSpel.tel_som_juiste_positie(gok)
        print("Je hebt {aantal_cijfers} cijfers geraden.")
        print("De som van de juist geraden cijfers is: {som_cijfers}.")
print("Jammer, de beurten zijn op. De correcte code was {CijferSpel}")

