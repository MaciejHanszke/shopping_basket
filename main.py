from basket import Basket
from constants import CATALOGUE

b1 = Basket()

b1.add(CATALOGUE['Baked Beans'])
b1.add(CATALOGUE['Baked Beans'])
b1.add(CATALOGUE['Baked Beans'])
b1.add(CATALOGUE['Baked Beans'])
b1.add(CATALOGUE['Biscuits'])

print("Basket 1:")
b1.checkout()

b2 = Basket()

b2.add(CATALOGUE['Baked Beans'])
b2.add(CATALOGUE['Baked Beans'])
b2.add(CATALOGUE['Biscuits'])
b2.add(CATALOGUE['Sardines'])
b2.add(CATALOGUE['Sardines'])

print("\nBasket 2:")
b2.checkout()

b3 = Basket()

b3.add(CATALOGUE['Shampoo (Large)'])
b3.add(CATALOGUE['Shampoo (Large)'])
b3.add(CATALOGUE['Shampoo (Large)'])
b3.add(CATALOGUE['Shampoo (Medium)'])
b3.add(CATALOGUE['Shampoo (Small)'])
b3.add(CATALOGUE['Shampoo (Small)'])

print("\nBasket 3:")
b3.checkout()