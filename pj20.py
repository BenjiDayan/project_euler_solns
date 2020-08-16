#pj20

def factorial(n):
    comp = 1
    for num in range(1, n+1):
        comp *= num
    return(comp)

def digit_sum(n):
    """Returns the sum of the digits of n"""
    a = str(n)
    dsum = 0
    for char in a:
        dsum += int(char)

    return(dsum)
