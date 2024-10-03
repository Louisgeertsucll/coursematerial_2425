# write your code here
from math import floor,ceil
def buses_needed(people_count,bus_capacity):
    x= ceil(people_count/bus_capacity)
    return x
print(buses_needed(20,7))
