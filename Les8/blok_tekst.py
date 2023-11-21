#%%
def blok_tekst(zin):
    zin_zonder_spatie = zin.replace(" ", "")
    lengte_zin = len(zin_zonder_spatie)
    i = 0
    nieuwe_zin = ""

    while i < lengte_zin:
        blok = zin_zonder_spatie[i:i+5]
        nieuwe_zin = f"{nieuwe_zin} {blok}"
        i += 5
    return nieuwe_zin

blok_tekst("Een korte maar wel een echte zin")
# %%
