#%%
def faculteit(n):
    if n == 0:
        return 1
    else:
        resultaat = 1
        for i in range(1, n + 1):
            resultaat *= i
        return resultaat

def reeks(x):
    n = 0
    benadering = 0
    term = 1
    
    while term >= 1e-6:
        benadering += term
        n += 1
        term = x**n / faculteit(n)
    
    return benadering

x = float(input("Voer de waarde van x in: "))
resultaat = reeks(x)
print(f"Benadering van e^{x} is: {resultaat}")
# %%
