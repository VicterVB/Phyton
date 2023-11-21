#%%
def patroon(hoogte):
    hoogte = None if (hoogte % 2) != 0 else hoogte
    for i in range(hoogte):
        slash = "\\\t/" if (i % 2) == 0 else "/\t\\"
        i += 1
        print(slash)

patroon(4)
# %%
def tekenreeks(lengte, hoogte, karakter):
    for i in range(hoogte):
        print(karakter * lengte)
        print("")

tekenreeks(8,3,":) ")

# %%
def kerstboom(hoogte):
    for i in range(hoogte + 1):
        print("*" * i)

kerstboom(7)
# %%
def driehoek(hoogte):
    for i in range(hoogte + 1):
        rechts = "*" * i
        links = rechts[:i - 1 ].rjust(hoogte - 1, " ")
        print(f"{links}{rechts}")


driehoek(8)
# %%
