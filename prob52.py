import sys

def reordered(num1, num2):
    """Returns True if two are reorderings of each other, otherwise False"""
    a, b = [list(str(num1)), list(str(num2))]
    for char in a:
        try:
            b.remove(char)
        except ValueError:
            return(False)
    
    return(b == [])

def check_mult(num, maxmult):
    """Checks 2*num, ..., maxmult*num to see if are reorderings. Returns the number of matches"""
    count = 0
    for mult in range(2, maxmult+1):
        if reordered(num, mult*num):
            count += 1
    return(count)


def seek(maxpower, maxmult):
    foo = [0, 0]
    
    for power in range(maxpower):
        for num in range(int(10**power), 2*int(10**power)):
            a = check_mult(num, maxmult)
            if a >= foo[1]:
                foo = [num, a] 
           
            if a == maxmult-1:
                return(num)

        print("power is {0}, foo is {1}".format(power, foo))
    return(foo)
