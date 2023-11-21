#%%
def eerste_karakter(woord):
    if woord[0].isupper() or woord[0].islower() or woord[0].isnumeric():
        return True
    else:
        return False

eerste_karakter("-allo")
# %%
import string

def aantal_hoofdletters (zin):
    if type(zin) == str: 
        hoofdletters = string.ascii_uppercase
        count = 0

        for letter in zin:
            count += 1 if letter in hoofdletters else 0

        return count
    else:
        print("Het invoer is geen zin. ")

aantal_hoofdletters("Hallo")
# %%
def even_oneven_woord(woord):
    if len(woord) % 2 == 0:
        return woord.upper()
    else:
        return woord.lower()
    
even_oneven_woord("Hallo")
even_oneven_woord("test")
# %%
import string

def pangram(zin):
    alphabet = string.ascii_lowercase
    for char in alphabet:
        if char not in zin.lower():
            return False
    return True

pangram("The quick brown fox jumps over the lazy dog")
# %%
def maand_maandnummer(invoer):
    def maand(maandnummer):
        if maandnummer == 1:
            maand = "Januari"
        elif maandnummer == 2:
            maand = "Februari"
        elif maandnummer == 3:
            maand = "Maart"
        elif maandnummer == 4:
            maand = "April"
        elif maandnummer == 5:
            maand = "Mei"
        elif maandnummer == 6:
            maand = "Juni"
        elif maandnummer == 7:
            maand = "Juli"
        elif maandnummer == 8:
            maand = "Augustus"
        elif maandnummer == 9:
            maand = "September"
        elif maandnummer == 10:
            maand = "Oktober"
        elif maandnummer == 11:
            maand = "November"
        elif maandnummer == 12:
            maand = "December"
        else:
            print("De invoer is geen getal die een maand voorsteldt.")
            return
        return maand
    
    def maandnummer(maand):
        if maand == "Januari":
            maandnummer = 1
        elif maand == "Februari":
            maandnummer = 2
        elif maand == "Maart":
            maandnummer = 3
        elif maand == "April":
            maandnummer = 4
        elif maand == "Mei":
            maandnummer = 5
        elif maand == "Juni":
            maandnummer = 6
        elif maand == "Juli":
            maandnummer = 7
        elif maand == "Augustus":
            maandnummer = 8
        elif maand == "September":
            maandnummer = 9
        elif maand == "Oktober":
            maandnummer = 10
        elif maand == "November":
            maandnummer = 11
        elif maand == "December":
            maandnummer = 12
        else:
            print("De invoer is geen maand die bestaat")
            return
        return maandnummer
    
    if type(invoer) == int:
        uitkomst = maand(invoer)
    else:
        uitkomst = maandnummer(invoer)
    return uitkomst

maand_maandnummer(11)
# %%
import math
def kortste_string():
    vorige_len = math.inf
    while True:
        invoer = str(input("Geef een string, vul 'stop' in om te stoppen."))
        if (len(invoer) < vorige_len) and (invoer != "stop"):
            vorige_len = len(invoer)
            kortste_woord = invoer
        elif invoer == "stop":
            return kortste_woord

    
kortste_string()
