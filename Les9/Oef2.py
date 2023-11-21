#%%
tuple1 = (1, 2, 3)
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3[0])
print(tuple3[-1])
print(tuple3[0:3])

print(sum(tuple3))
tuple3_lijst = list(tuple3)
tuple3_lijst.sort()
print(tuple3_lijst[-1])
print(tuple3_lijst[0])
# %%
