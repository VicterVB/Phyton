#%%
def ggd(getal1, getal2):
    while getal2:
        getal1, getal2 = getal2, getal1 % getal2
    return getal1

print(ggd(60, 600))

def kgv(getal1, getal2):
    return (getal1 * getal2) // ggd(getal1, getal2)

print(kgv(12, 18))
# %%
