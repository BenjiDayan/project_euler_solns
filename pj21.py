#pj21

import math

def amicable(x, y):
    """Returns true if x and y are amicable.
    Let d(n) be defined as the sum of proper divisors of n
    (numbers less than n which divide evenly into n).
    Amicable means that d(x) = y and d(y) = x."""

    a = sum(proper_divisors(x))
    b = sum(proper_divisors(y))
    
    if a == y and b == x:
        return(True)
    else:
        return(False)
    
def proper_divisors(x):
    """Returns the list of proper divisors of x, numbers
    less than n which divide evenly into x."""
    comp = []
    for num in range(1, math.floor(x/2) + 1):
        if x % num == 0:
                comp.append(num)
        
    return(comp)


comp = []
for num in range(1, 20000):
    if num % 100 == 0:
       print(num)
    a = sum(proper_divisors(num))
    if sum(proper_divisors(a)) == num and (not a == num):
        comp.append([a, num])
