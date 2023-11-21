#%%
T1 = 1
T2 = 2
T1_VAST = 75
T2_VAST = 50
BTW = 6

verbruik = int(input("Wat is het verbruik? in m³" ))
tarief = int(input("Wat is de tariefcode? "))

if tarief == 1:
    bedrag = (T1_VAST + T1 * verbruik)
    bedrag = bedrag + (bedrag / 100) * 6
else:
    bedrag = (T2_VAST + T2 * verbruik)
    bedrag = bedrag + (bedrag / 100) * 6

print(f"Het totale bedrag is €{bedrag}")
