#%%
def plus_min_som(n):
    s = 0
    for i in range(1, n + 1):
        if i % 2 == 1:
            s += i  # Voeg de oneven getallen toe
        else:
            s -= i  # Trek de even getallen af
    return s

# Voorbeeldgebruik:
n = int(input("Voer een getal n in: "))
resultaat = plus_min_som(n)
print(f"Het resultaat van de som is: {resultaat}")
# %%
