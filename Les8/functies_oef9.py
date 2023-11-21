# %%
def min_max_klinkers():
    N = 5  # Definieer het aantal woorden dat moet worden ingevoerd als constante

    def tel_klinkers(woord):
        klinkers = "aeiouAEIOU"
        count = 0

        for letter in woord:
            count += 1 if letter in klinkers else 0

        return count

    min_aantal_klinkers = float('inf')
    max_aantal_klinkers = 0
    min_woord = ""
    max_woord = ""

    for i in range(N):
        woord = input(f"Voer woord {i + 1} in: ")
        aantal_klinkers = tel_klinkers(woord)

        min_aantal_klinkers, min_woord = (aantal_klinkers, woord) if aantal_klinkers < min_aantal_klinkers else (min_aantal_klinkers, min_woord)
        max_aantal_klinkers, max_woord = (aantal_klinkers, woord) if aantal_klinkers > max_aantal_klinkers else (max_aantal_klinkers, max_woord)

    print(f"Minst aantal klinkers: {min_woord}")
    print(f"Meest aantal klinkers: {max_woord}")

# Roep de functie aan om woorden in te voeren en minst en meest aantal klinkers te vinden
min_max_klinkers()
#%%
n = 5

def verschillende_klinkers(woord):
    klinkers = "aeiouAEIOU"
    return len(set(filter(lambda letter: letter in klinkers, woord)))

def min_max_klinkers():
    min_aantal = float('inf')
    max_aantal = 0
    min_woord = ""
    max_woord = ""

    for _ in range(n):
        woord = input("Voer een woord in: ")
        aantal = verschillende_klinkers(woord)

        if aantal < min_aantal:
            min_aantal, min_woord = aantal, woord
        elif aantal > max_aantal:
            max_aantal, max_woord = aantal, woord

    print(f"Minst aantal verschillende klinkers: {min_woord}")
    print(f"Meest aantal verschillende klinkers: {max_woord}")

min_max_klinkers()
# %%
