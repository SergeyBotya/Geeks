prices = [57.8, 46.51, 97, 38.69, 150, 286.14, 2980, 13.99, 29.5, 2022]

# A
for i in range(len(prices)):
    price = (str(prices[i]).split('.'))
    if type(prices[i]) == int:
        print(f'"{(price[0])} руб, 00 коп"')
    else:
        print(f'"{price[0]} руб, {price[1].zfill(2)} коп"')
print(id(prices))
print()

# B
prices.sort()
for i in range(len(prices)):
    price = (str(prices[i]).split('.'))
    if type(prices[i]) == int:
        print(f'"{(price[0])} руб, 00 коп"')
    else:
        print(f'"{price[0]} руб, {price[1].zfill(2)} коп"')
print(id(prices))
print()

# C
from copy import deepcopy
new_prices = deepcopy(prices)
new_prices.reverse()
print(new_prices)
print()

# D
for i in range(5):
    price = (str(new_prices[i]).split('.'))
    if type(new_prices[i]) == int:
        print(f'"{(price[0])} руб, 00 коп"')
    else:
        print(f'"{price[0]} руб, {price[1].zfill(2)} коп"')