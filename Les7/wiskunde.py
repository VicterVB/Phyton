#%%
def tafels():
    for i in range(1,11):
        print("De tafel van", i)
        for i2 in range (1,11):
            print( i * i2)
 
tafels()
#%%
def kwadraat_en_gemiddelde():
    getallen = []
    totaal = 0

    for i in range(7):
        getal = float(input(f"Voer getal {i + 1} in: "))
        kwadraat = getal ** 2
        getallen.append(kwadraat)
        totaal += getal

    gemiddelde = totaal / 7

    for i, kwadraat in enumerate(getallen):
        print(f"Getal {i + 1}: {kwadraat}")

    print(f"Gemiddelde: {gemiddelde}")

kwadraat_en_gemiddelde()

#%%
def is_priemgetal(n):
    """ Controleren of een gegeven nummer n een priemgetal is of niet """

    while n == 2:
        return
    
    for i in range(2,n):
        uitkomst = False if n % i == 0 else True
    return uitkomst

is_priemgetal(17)
# %%
def fibonnaci(invoer):
    Fn_1 = 0
    Fn_2 = 1
    invoer += 1

    for i in range(3, invoer + 1, 1):
        Fn = Fn_2 + Fn_1
        Fn_2 = Fn_1
        Fn_1 = Fn
    print(str(Fn))

fibonnaci(6)
# %%