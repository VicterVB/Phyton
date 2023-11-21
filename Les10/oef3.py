import random
getallen = {"1":0, "2":0, "3":0, "4":0, "5":0, "6":0, "7":0, "8":0, "9":0}

for i in range(100):
    getal = str(random.randint(1,9))
    if getal in getallen:
        getallen[getal] += 1
        
print(getallen)