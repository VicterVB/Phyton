class Teller:
    def __init__(self, data = []):
        self.data = data

    def plus(self, argm):
        print("Nog niet geïmplementeerd")

    def __add__(self, argm):
        if isinstance(argm, Teller):
            return Teller(self.data + argm.data)
    
    def __radd__(self, argm):
        if isinstance(argm, Teller):
            return Teller(argm.data + self.data)

class LijstTeller(Teller):
    def plus(self, argm):
        if isinstance(argm, list):
            self.data.extend(argm)

class DictTeller(Teller):
    def plus(self, argm):
        if isinstance(argm, dict):
            self.data.update(argm)

# Demonstratie
teller1 = LijstTeller([1, 2, 3])
teller2 = DictTeller({'a': 10, 'b': 20})
teller3 = Teller([4, 5])

# Gebruik van de plus-methode
teller1.plus([6, 7, 8])
teller2.plus({'c': 30})
teller3.plus([9, 10])

# Gebruik van de __add__-methode
resultaat1 = teller1 + teller2
resultaat2 = teller2 + teller3
resultaat3 = teller1 + teller3

# Gebruik van de __radd__-methode
resultaat4 = [1, 2, 3] + teller1

# Uitvoer
print("Teller 1 data:", teller1.data)
print("Teller 2 data:", teller2.data)
print("Teller 3 data:", teller3.data)

print("Resultaat 1 data:", resultaat1.data)
print("Resultaat 2 data:", resultaat2.data)
print("Resultaat 3 data:", resultaat3.data)
print("Resultaat 4 data:", resultaat4.data)