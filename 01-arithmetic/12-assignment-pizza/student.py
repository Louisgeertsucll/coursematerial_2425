# write your code here
from math import floor,ceil
def pizza(n_people, slices_per_pizza):
    x=ceil(n_people/slices_per_pizza)
    return x
print(pizza(28,9))