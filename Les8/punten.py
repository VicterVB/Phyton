#%%
t = int(input("Wat was het resultaat van de Theorie test? (geef enkel jouw behaald cijfer niet het te behalen cijfer)"))
p = int(input("Wat was het resultaat van de Praktijk test? (geef enkel jouw behaald cijfer niet het te behalen cijfer)"))

if p < t:
    c = p
else:
    c = (p + t) / 2

print(f"Het eindersultaat is {c}") 
# %%
t = int(input("Wat was het resultaat van de Theorie test? (geef enkel jouw behaald cijfer niet het te behalen cijfer)"))
p = int(input("Wat was het resultaat van de Praktijk test? (geef enkel jouw behaald cijfer niet het te behalen cijfer)"))

c = p if p < t else (p + t) / 2
print(f"Het eindersultaat is {c}") 
# %%
