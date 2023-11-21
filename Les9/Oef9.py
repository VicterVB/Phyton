#%%
def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def get_prime_numbers(n):
    prime_numbers = []
    for i in range(2, n):
        if is_prime(i):
            prime_numbers.append(i)
    return prime_numbers

n = int(input("Voer een getal n in: "))
prime_list = get_prime_numbers(n)

print("Priemgetallen kleiner dan", n, "zijn:", prime_list)

# %%
