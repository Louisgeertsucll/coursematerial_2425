# write your code here
def coins(amount):
    five_x=amount//5
    r_x=amount-(five_x*5)
    two_y=r_x//2
    r_x-= (two_y*2)
    one_x=r_x
    total=five_x+two_y+one_x
    return total
