class Rechthoek:
    def __init__(self, cord = [0,0], breedte = 1, lengte = 1):
        self.cord = cord
        self.breedte = breedte
        self.lengte = lengte

    def is_vierkant(self):
        if self.lengte == self.breedte:
            return True
        else: return False

    def bereken_omtrek(self):
        omtrek = (self.lengte * 2) + (self.breedte * 2)
        return omtrek
    
    def bereken_opp(self):
        opp = self.breedte * self.lengte
        return opp
    
    def is_in(self, cord_punt):
        if cord_punt[0] >= self.cord[0] and cord_punt[0] <= self.cord[0] + self.breedte and \
           cord_punt[1] >= self.cord[1] and cord_punt[1] <= self.cord[1] + self.lengte:
            return True
        else: return False

    def __str__(self):
        cord_l_boven = self.cord
        cord_l_onder = [cord_l_boven[0],cord_l_boven[1] + self.breedte]
        cord_r_boven = [cord_l_boven[0] + self.lengte,cord_l_boven[1]]
        cord_r_onder = [cord_l_onder[0] + self.lengte,cord_l_onder[1]]
        return f"linksboven:{cord_l_boven}, linksonder:{cord_l_onder}, \
rechtsboven:{cord_r_boven}, rechtsonder:{cord_r_onder}"

rechthoek = Rechthoek([2, 3], 4, 5)

print(rechthoek)
print(f"Is een vierkant: {rechthoek.is_vierkant()}")
print(f"Omtrek: {rechthoek.bereken_omtrek()}")
print(f"Oppervlakte: {rechthoek.bereken_opp()}")

x_punt = int(input("Geef de x-coördinaat van een punt: "))
y_punt = int(input("Geef de y-coördinaat van een punt: "))

if rechthoek.is_in((x_punt, y_punt)):
    print(f"Het punt ({x_punt}, {y_punt}) bevindt zich in de rechthoek.")
else:
    print(f"Het punt ({x_punt}, {y_punt}) bevindt zich niet in de rechthoek.")