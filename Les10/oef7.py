def sorteer_lijsten(invoer):
    gesorteerde = {}
    for key, value in invoer.items():
        gesorteerde[key] = sorted(value, reverse=True)
    return gesorteerde

def lengte_lijsten(invoer):
    lengte = {}
    for key, value in invoer.items():
        lengte[key] = len(value)
    return lengte

def gemid_lijsten(invoer):
    gemid = {}
    for key, value in invoer.items():
        gemid[key] = sum(value) / len(value)
    return gemid

def verwijder_lege_lijsten(invoer):
    new_lijst = {}
    for key, value in invoer.items():
        if value != []:
            new_lijst[key] = value
    return new_lijst

num = {'n1': [2, 3, 1], 'n2': [5, 1, 2, 7], 'n3': [3, 4]}

print(sorteer_lijsten(num))
print(lengte_lijsten(num))
print(gemid_lijsten(num))
num['n4'] = []
print(verwijder_lege_lijsten(num))