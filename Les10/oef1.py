keys = ["a", "b", "c"]
values = [1, 2, 3]

my_dict = dict(zip(keys, values))
print(my_dict)

my_dict["d"] = 4
print(my_dict)

del my_dict["a"]
print(my_dict)

my_dict["b"] = 5
print(my_dict)

if "c" in my_dict:
    print("c zit in de dictionary")

for key in my_dict:
    print(key)

for key in my_dict:
    print(my_dict[key],)