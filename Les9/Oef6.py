#%%
import random

lijst = []
nul,posi,nega = 0,0,0

for i in range(100):
    lijst += [random.randint(-50,50)]
    if lijst[i] == 0:
        nul += 1
    elif lijst[i] > 0:
        posi += 1
    else:
        nega += 1

print(f"Er zijn {nega} negatieve getallen, {posi} positieve gatellen en {nul} keer nul")
# %%
