# write your code here
def coins(amount):
    x=(amount//5)
    x=(x-amount)
    y=(amount//2)
    y=(y-amount)
    z=amount-(y+x)
    z=z+x+y
    return z
