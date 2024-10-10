# write your code here
def close_enough(x,y):
    z=(x-y)
    if -0.1<=z<=0.1:
        return True
    else:
        return False
    