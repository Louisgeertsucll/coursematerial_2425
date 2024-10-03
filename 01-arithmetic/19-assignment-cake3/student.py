# write your code hereµ
def cake3(eggs, flour, butter, sugar):
    x=(eggs//5)
    y=(flour//250)
    x1=(butter//200)
    y2=(sugar//250)
    z=min(x,y,x1,y2)
    return z
print(cake3(5,250,200,250))