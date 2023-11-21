#%%
def increase_elements_with_loop(input_list):
    result = []
    for num in input_list:
        result.append(num + 1)
    return result

def increase_elements_with_list_comprehension(input_list):
    return [num + 1 for num in input_list]

def sum_of_squares_with_loop(n):
    result = 0
    for i in range(1, n + 1):
        result += i**2
    return result
    
def sum_of_squares_with_list_comprehension(n):
    return sum([i**2 for i in range(1, n + 1)])

def get_divisors_with_loop(num):
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)
    return divisors

def get_divisors_with_list_comprehension(num):
    return [i for i in range(1, num + 1) if num % i == 0]

# Voor de eerste functie
input_list = [1, 2, 3, 4, 5]
result_with_loop = increase_elements_with_loop(input_list)
result_with_list_comprehension = increase_elements_with_list_comprehension(input_list)

# Voor de tweede functie
n = 5
result_with_loop = sum_of_squares_with_loop(n)
result_with_list_comprehension = sum_of_squares_with_list_comprehension(n)

# Voor de derde functie
num = 12
result_with_loop = get_divisors_with_loop(num)
result_with_list_comprehension = get_divisors_with_list_comprehension(num)


# %%
