class Pizza:
    def __init__(self, size, toppings):
        self.size = size
        self.toppings = toppings

    def __str__(self):
        topping = self.toppings[0]
        for arg in self.toppings[1:]:
            topping += f" en {arg}"
        return f"Een {self.size} pizza met {topping}"

    def __add__(self, other):
        if isinstance(other, Pizza):
            size = "Medium" if self.size == "Medium" and Pizza.size == "Medium" else "Large"
            toppings = self.toppings + other.toppings
            return Pizza(size, toppings)

    def __len__(self):
        return len(self.toppings)

    def is_aanwezig(self, toppings):
        waarde = []
        for topping in toppings:
            if topping not in self.toppings:
                waarde.append(False)
            else: waarde.append(True)
        return waarde



napoli_medium = Pizza('medium',['anjovis','kappertjes', 'olijven'])
hawai_large = Pizza('large',['ananas','gekookte ham'])

print(napoli_medium)

print(hawai_large)

combinatie = napoli_medium + hawai_large
print(combinatie)

print(len(combinatie))

print(combinatie.is_aanwezig(["peperoni", "ananas","champignons"]))