# write your code here
from math import ceil
def drop_last_digit(n):
    x=(n%10)
    z=n//x
    return ceil(z)