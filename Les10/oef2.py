fruit_kleuren = {"Appel":"Rood", "Banaan":"Geel", "Kers":"Rood", "Druif":"Paars", "Citroen":"Geel"}

print(fruit_kleuren["Druif"])

for key in fruit_kleuren:
    print(key)

for key in fruit_kleuren:
    print(fruit_kleuren [key],)

fruit_kleuren["Appel"] = "Groen"
print(fruit_kleuren)

fruit_kleuren["Appelsien"] = "Oranje"
print(fruit_kleuren)

print(fruit_kleuren.pop("Citroen"))

if "Ananas" in fruit_kleuren:
    print("Ananas zit in de dictionary")
else:
    fruit_kleuren["Ananas"] = "Geel"
print(fruit_kleuren)