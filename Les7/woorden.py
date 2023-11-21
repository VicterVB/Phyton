#%%
def plak_alles_samen():
    woorden = 0
    n_woorden = int(input("Hoeveel woorden wil je inlezen? "))
    zin = ''

    while woorden < n_woorden:
        woord = input("Geef een woord: ")
        zin = zin + ''.join(woord)
        woorden += 1
    
    len_zin = len(zin)
    return len_zin

plak_alles_samen()
# %%
def af_en_op(woord):
    n = len(woord) +1

    for i in range(n, 0, -1):
        print(woord[:i])
    
    for i in range(2, n):
        print(woord[:i])

af_en_op("MARSEPEIN")
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

# %%

# %%
