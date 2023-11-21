#%%
import string

def count_letters(woord):
    teller_klein = 0
    teller_groot = 0
    for k in woord:
        if k in string.ascii_lowercase:
            teller_klein += 1
        if k in string.ascii_uppercase:
            teller_groot += 1
    return teller_klein, teller_groot

count_letters("HeLlo")
# %%
