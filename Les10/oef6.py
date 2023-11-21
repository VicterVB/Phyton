import random
def quiz(dictionary):
    while True:
        postcode = random.choice(list(dictionary.keys()))
        oplossing = dictionary[postcode]
        antwoord = input(f"Wat is de gemeente die bij de postcode {postcode} hoort? ")
        antwoord_upper = antwoord.capitalize()
        if antwoord == "Stop":
            break
        elif antwoord_upper in oplossing:
            print("Correct!")
            vraag = input("Wil je verder spelen? (y/n) ")
            if vraag == "n":
                break
        else:
            print("Opnieuw!")
        


postnummers = [
    8550, 9000, 9030, 9031, 9032, 9040, 9041, 9042, 9042, 9042, 9050, 9050, 9051, 9051, 9052
]

gemeenten = [
    "Zwevegem", "Gent", "Mariakerke", "Drongen", "Wondelgem", "Sint-amandsberg",
    "Oostakker", "Desteldonk", "Mendonk", "Sint-kruis-winkel", "Ledeberg", "Gentbrugge",
    "Sint-denijs-westrem", "Afsnee", "Zwijnaarde"
]

postnummers_en_gemeenten = {}

for postnummer, gemeente in zip(postnummers, gemeenten):
    if postnummer in postnummers_en_gemeenten:
        postnummers_en_gemeenten[postnummer].append(gemeente)
    else:
        postnummers_en_gemeenten[postnummer] = [gemeente]

print(postnummers_en_gemeenten)

quiz(postnummers_en_gemeenten)