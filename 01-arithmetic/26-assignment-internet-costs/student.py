# write your code here
from math import ceil
def internet_costs(duration_in_seconds,cost_per_block):
  x=duration_in_seconds//360
  y=(duration_in_seconds%360)/360
  z=ceil(y)
  total=(x+z)*cost_per_block
  return total

    