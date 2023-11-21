leeftijden = {}
while True:
    invoer = input("Geef een naam en geboortje jaar bv. (Kermit,1955) of stop: ")
    if invoer == "stop":
        print(leeftijden)
        break
    else:
        naam, jaar = invoer.split(",")
        leeftijden[naam] = int(jaar)

oudste_naam = ""
jongste_naam = ""
oudste_leeftijd = 2023
jongste_leeftijd = 0

for naam, leeftijd in leeftijden.items():
    if leeftijd > jongste_leeftijd:
        jongste_naam = naam
        jongste_leeftijd = leeftijd
    if leeftijd < oudste_leeftijd:
        oudste_naam = naam
        oudste_leeftijd = leeftijd

print(f"De oudste persoon is {oudste_naam} en is {2023 - oudste_leeftijd} jaar oud.")
print(f"De jongste persoon is {jongste_naam} en is {2023 - jongste_leeftijd} jaar oud.")