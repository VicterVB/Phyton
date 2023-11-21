#%%
def roman_calculator(dictionaty, invoer):
    uitkomst = 0
    voorige_waarde = 0
    
    for cijfer in reversed(invoer):
        waarde = dictionaty[cijfer]

        if waarde < voorige_waarde:
            uitkomst -= waarde
        else:
            uitkomst += waarde

        voorige_waarde = waarde

    return uitkomst

romeinse_cijfers = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}

print(roman_calculator(romeinse_cijfers, "IIX"))
