#%% Deel 1
def alle_pos_getallen(lijst):
    """Kijkt of de getallen van de lijst positief zijn."""
    for i in lijst:
        if type(i) == str or i < 0:
            return False
    return True
    
print(alle_pos_getallen([5,12.45,1000,27.4,0]))
print(alle_pos_getallen([5,"12.45",1000,27.4,0]))
print(alle_pos_getallen([5,12.45,1000,-27.4,0]))


def som_lijsten(lijst1, lijst2):
    """Telt de twee lijsten op als alle getallen positief zijn en de lijst de zelfde lengte hebben."""
    som = []
    if len(lijst1) == len(lijst2):
        for i in range(len(lijst1)):
            if alle_pos_getallen(lijst1) and alle_pos_getallen(lijst2):
                som.append(lijst1[i] + lijst2[i])
            else:
                som = []
    return som
        
print(som_lijsten([1,2,3], [4,5,6,7]))
print(som_lijsten([1,2,3], [4,5,6,]))
print(som_lijsten(["1","2","3"], ["4","5","6"]))


def dag_van_de_week(dag):
    """Zet de dag om naar het getal dat overeen komt met die dag. """
    if dag == "maandag":
        return 1
    elif dag == "dinsdag":
        return 2
    elif dag == "woensdag":
        return 3
    elif dag == "donderdag":
        return 4
    elif dag == "vrijdag":
        return 5
    elif dag == "zaterdag":
        return 6
    elif dag == "zondag":
        return 7
    else:
        return False
    
print(dag_van_de_week("donderdag"))
print(dag_van_de_week("luiedag"))


# %% Deel 2
def alle_pos_getallen(lijst):
    """Kijkt of de getallen van de lijst positief zijn."""
    for i in lijst:
        if type(i) == str or i < 0:
            return False
    return True

class Webshop:
    def __init__(self, naam_webshop, jaartal = 2023, verkoop = {}):
        self.naam_webshop = naam_webshop
        self.jaartal = jaartal
        self.verkoop = verkoop

    def voeg_week_toe(self, week, verkoopcijfer):
        if week <= 1 and week >= 52:
            print("De ingegeven week is niet correct!!")
        elif len(verkoopcijfer) != 7 or alle_pos_getallen(verkoopcijfer) == False:
            print(f"De ingegeven lijst {verkoopcijfer} is niet correct!!")
        else:
            self.verkoop[week] = verkoopcijfer

    def __str__(self):
        return f"De webshop is: {self.naam_webshop} \nHet jaartal is {self.jaartal} \nDe beschikbare weken en hun verkoopcijfers zijn: {self.verkoop}"
    
week9 = [1245.67, 1490.07, 1679.87, 237.46, 1783.92, 1461.99, 2059.77]
week10 = [2541.36, 2965.88, 1965.32, 1845.23, 7021.11, 9652.74, 1469.36]
week13 = [2513.45, 1963.22, 1568.35, 1966.35, 1893.25, 1025.36, 1128.36]
week16 = [2589.55, 1970.26, 1468.70, 1950.05, 3800.25, 1250.16, 1111.16]
week17 = [5500.56, 5065.80, 5565.30, -5545.23, 5021.11, 5530.60, 5485.12]

test = Webshop("test_webshop")
test.voeg_week_toe(9, week9)
test.voeg_week_toe(10, week10)
test.voeg_week_toe(13, week13)
test.voeg_week_toe(16, week16)
test.voeg_week_toe(17, week17)

print(test)


# %% Deel 3
def alle_pos_getallen(lijst):
    """Kijkt of de getallen van de lijst positief zijn."""
    for i in lijst:
        if type(i) == str or i < 0:
            return False
    return True
    
def dag_van_de_week(dag):
    """Zet de dag om naar het getal dat overeen komt met die dag. """
    if dag == "maandag":
        return 1
    elif dag == "dinsdag":
        return 2
    elif dag == "woensdag":
        return 3
    elif dag == "donderdag":
        return 4
    elif dag == "vrijdag":
        return 5
    elif dag == "zaterdag":
        return 6
    elif dag == "zondag":
        return 7
    else:
        return False
    
class Webshop:
    def __init__(self, naam_webshop, jaartal = 2023, verkoop = {}):
        self.naam_webshop = naam_webshop
        self.jaartal = jaartal
        self.verkoop = verkoop

    def voeg_week_toe(self, week, verkoopcijfer):
        if week <= 1 and week >= 52:
            print("De ingegeven week is niet correct!!")
        elif len(verkoopcijfer) != 7 or alle_pos_getallen(verkoopcijfer) == False:
            print(f"De ingegeven lijst {verkoopcijfer} is niet correct!!")
        else:
            self.verkoop[week] = verkoopcijfer

    def geef_week_gemiddelde(self, week):
        if week in self.verkoop:
            return round(sum(self.verkoop[week]) / len(self.verkoop[week]), 2)
        else:
            return "Geen gegevens beschikbaar"
        
    def geef_dagg_gemiddelde(self, dag):
        gem = 0
        dag_nummer = dag_van_de_week(dag)
        for i in self.verkoop:
            week = self.verkoop[i]
            gem += week[dag_nummer - 1]
        gem /= len(self.verkoop)
        return round(gem, 2)

    def __str__(self):
        return f"De webshop is: {self.naam_webshop} \nHet jaartal is {self.jaartal} \nDe beschikbare weken en hun verkoopcijfers zijn: {self.verkoop}"
    
week9 = [1245.67, 1490.07, 1679.87, 237.46, 1783.92, 1461.99, 2059.77]
week10 = [2541.36, 2965.88, 1965.32, 1845.23, 7021.11, 9652.74, 1469.36]
week13 = [2513.45, 1963.22, 1568.35, 1966.35, 1893.25, 1025.36, 1128.36]
week16 = [2589.55, 1970.26, 1468.70, 1950.05, 3800.25, 1250.16, 1111.16]
week17 = [5500.56, 5065.80, 5565.30, -5545.23, 5021.11, 5530.60, 5485.12]

test = Webshop("test_webshop")
test.voeg_week_toe(9, week9)
test.voeg_week_toe(10, week10)
test.voeg_week_toe(13, week13)
test.voeg_week_toe(16, week16)
test.voeg_week_toe(17, week17)

# print(test)

print(test.geef_week_gemiddelde(16))
print(test.geef_dagg_gemiddelde("zondag"))

# %% Deel 4
def alle_pos_getallen(lijst):
    """Kijkt of de getallen van de lijst positief zijn."""
    for i in lijst:
        if type(i) == str or i < 0:
            return False
    return True
    
def dag_van_de_week(dag):
    """Zet de dag om naar het getal dat overeen komt met die dag. """
    if dag == "maandag":
        return 1
    elif dag == "dinsdag":
        return 2
    elif dag == "woensdag":
        return 3
    elif dag == "donderdag":
        return 4
    elif dag == "vrijdag":
        return 5
    elif dag == "zaterdag":
        return 6
    elif dag == "zondag":
        return 7
    else:
        return False
    
def som_lijsten(lijst1, lijst2):
    """Telt de twee lijsten op als alle getallen positief zijn en de lijst de zelfde lengte hebben."""
    som = []
    if len(lijst1) == len(lijst2):
        for i in range(len(lijst1)):
            if alle_pos_getallen(lijst1) and alle_pos_getallen(lijst2):
                som.append(lijst1[i] + lijst2[i])
            else:
                som = []
    return som

class Webshop:
    def __init__(self, naam_webshop, jaartal = 2023, verkoop = {}):
        self.naam_webshop = naam_webshop
        self.jaartal = jaartal
        self.verkoop = verkoop

    def voeg_week_toe(self, week, verkoopcijfer):
        if week <= 1 and week >= 52:
            print("De ingegeven week is niet correct!!")
        elif len(verkoopcijfer) != 7 or alle_pos_getallen(verkoopcijfer) == False:
            print(f"De ingegeven lijst {verkoopcijfer} is niet correct!!")
        else:
            self.verkoop[week] = verkoopcijfer

    def geef_week_gemiddelde(self, week):
        if week in self.verkoop:
            return round(sum(self.verkoop[week]) / len(self.verkoop[week]), 2)
        else:
            return "Geen gegevens beschikbaar"
        
    def geef_dagg_gemiddelde(self, dag):
        gem = 0
        dag_nummer = dag_van_de_week(dag)
        for i in self.verkoop:
            week = self.verkoop[i]
            gem += week[dag_nummer - 1]
        gem /= len(self.verkoop)
        return round(gem, 2)
    
    def __add__(self, argm):
        if isinstance(argm, Webshop):
            for i in argm.verkoop.keys():                        
                if i in self.verkoop:
                    self.verkoop[i] = som_lijsten(self.verkoop[i], argm.verkoop[i])
                else:
                    self.verkoop[i] = argm.verkoop[i]                      
            return self.verkoop
        else:
            raise TypeError("Deze functie kan alleen met Webshop-objecten worden uitgevoerd")
        

    def __str__(self):
        return f"De webshop is: {self.naam_webshop} \nHet jaartal is {self.jaartal} \nDe beschikbare weken en hun verkoopcijfers zijn: {self.verkoop}"
    
week9 = [1245.67, 1490.07, 1679.87, 237.46, 1783.92, 1461.99, 2059.77]
week10 = [2541.36, 2965.88, 1965.32, 1845.23, 7021.11, 9652.74, 1469.36]
week13 = [2513.45, 1963.22, 1568.35, 1966.35, 1893.25, 1025.36, 1128.36]
week16 = [2589.55, 1970.26, 1468.70, 1950.05, 3800.25, 1250.16, 1111.16]
week17 = [5500.56, 5065.80, 5565.30, -5545.23, 5021.11, 5530.60, 5485.12]

test = Webshop("test_webshop")
test.voeg_week_toe(9, week9)
test.voeg_week_toe(10, week10)
test.voeg_week_toe(13, week13)
test.voeg_week_toe(16, week16)
test.voeg_week_toe(17, week17)

#print(test)

#print(test.geef_week_gemiddelde(16))
#print(test.geef_dagg_gemiddelde("zondag"))

week4 = [4, 4, 4, 4, 4, 4, 4]
week10 = [100_000, 100_000, 100_000, 100_000, 100_000, 100_000, 100_000]

test2 = Webshop("test_webshop")
test2.voeg_week_toe(4, week4)
test2.voeg_week_toe(10, week10)

combinatie = test + test2
print(combinatie)
# %%
