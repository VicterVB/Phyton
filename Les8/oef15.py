import random

def blad_steen_schaar():
    keuzes = ["Blad", "Steen", "Schaar"]
    computer_keuze = random.choice(keuzes)

    while True:
        speler_keuze = input("Maak je keuze: Blad, Steen of Schaar\n> ").strip().capitalize()
        if speler_keuze in keuzes:
            break
        else:
            print("Ongeldige keuze. Probeer opnieuw.")

    print(f"Speler koos {speler_keuze} - Computer koos {computer_keuze}")

    if speler_keuze == computer_keuze:
        print("=> Het is een gelijkspel!")
    elif (
        (speler_keuze == "Blad" and computer_keuze == "Steen") or
        (speler_keuze == "Steen" and computer_keuze == "Schaar") or
        (speler_keuze == "Schaar" and computer_keuze == "Blad")
    ):
        print("=> Jij hebt gewonnen!")
    else:
        print("=> Computer heeft gewonnen!")

blad_steen_schaar()
