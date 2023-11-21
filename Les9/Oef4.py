#%%
def klinkers(woord):
    uitkomst = []
    for k in woord:
        if k in "aeiou":
            uitkomst += k
    return uitkomst


lijst1 = ["b","r", "o", "o", "d"]
lijst2 = ["b", "e", "n", "e", "d", "e", "n"]
print(klinkers(lijst1))
print(klinkers(lijst2))
# %%
