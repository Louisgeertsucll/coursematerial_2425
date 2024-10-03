# write your code here
def hour(durataion):
    h=(3600)
    return (durataion//h)

def minutes(duration):
    h=(hour(duration))
    m=  (duration)-(3600*h)
    return  (m//60)

def second(duration):
   h=(hour(duration))
   m=(duration)-(h*3600)
   s=(duration)-(m*60)
   return s
