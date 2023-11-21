#%%
def separate(n):
    even_numbers = []
    odd_numbers = []

    for i in range(n):
        if i % 2 == 0:
            even_numbers.append(i)
        else:
            odd_numbers.append(i)

    return even_numbers, odd_numbers

n = int(input("Voer een getal n in: "))
even, odd = separate(n)

print("Even getallen kleiner dan", n, "zijn:", even)
print("Oneven getallen kleiner dan", n, "zijn:", odd)

# %%
