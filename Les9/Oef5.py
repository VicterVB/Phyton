#%%
groenten = ['Wortel', 'Broccoli', 'Spinazie', 'Sla', 'Tomaat']

groente = [groente for groente in groenten if len(groente) >= 6]

print(groente)
#groente.remove("Tomaat")
groente.pop(-1)
groente

groenten.sort()
groenten
# %%
