# write your code here
def hours(duration):
    h=(duration)//3600
    return (h)

def minutes(duration):
    x=hours(duration)*3600
    m= (duration)-(x)
    return  (m//60)

def seconds(duration):
   x=hours(duration)*3600
   y=minutes(duration)*60
   s=(duration)-(x+y)
   return (s)
