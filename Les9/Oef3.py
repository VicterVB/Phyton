#%%
data = ("John", "Doe", 28)
voornaam, achternaam, leeftijd = data

print(f"Welkom, {voornaam} {achternaam}. Je bent {leeftijd} jaar oud.")
# %%
info = ("Alice", "Blue", 30, "Amsterdam", "Nederland")
voornaam, achternaam, leeftijd, *_ = info
# *_ is bedoeld om de resterende waarden uit de tuple op te vangen die je niet nodig hebt.
print(f"Dit is {voornaam} {achternaam}. Ze is {leeftijd} jaar oud.")
# %%
