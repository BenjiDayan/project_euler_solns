# mathStuff

import math

#checked
def not_prime(num):
    """Returns False if the number is a prime. Otherwise returns the first
    factor of the number found"""
    
    if num == 2:
        return(False)
    if num == 1:
        return(1)
    bar = math.ceil(math.sqrt(num))
    for x in range(2, bar+1):
        if num % x == 0:
            return(x)
    return(False)
    #5 is True
    
def prime(num):
    return(not not_prime(num))

def prime_factors(num):
    """Dissects num into constitutent primes
    >>> prime_factors(24)
    [2, 2, 2, 3]
    >>> prime_factors(60)
    [2, 2, 3, 5]
    """
    myList = []

    if num == 1:
        return([])

    # If a is False, it's a prime, otherwise it's the first factor.
    a = not_prime(num)
    if not a:
        myList += [num]
    else:
        myList += prime_factors(a) + prime_factors(int(num/a))
    return(myList)

def prime_factorize(num):
    primeFactors = prime_factors(num)
    prime_dir = {}
    for prime in primeFactors:
        try:
            prime_dir[prime] += 1
        except KeyError:
            prime_dir[prime] = 1

    return(prime_dir)
            
        

def recombine_factors(myList):
    """Takes list of number power pairs (x, y) and returns product of all x^y"""
    c = 1
    for thing in myList:
        c *= math.pow(thing[0], thing[1])
    return(c)



def highest_conglomerate(myList):
    """Takes myList of the form of many (x, y) and conglomerates them by
    sorting by x, and then merging into many (x, highest x's y)
    E.g. takes [(2, 4), (2, 3), (3, 1)] and makes it [(2,4), (3,1)]"""
    yo = myList
    yo.sort()
    length = len(yo)
    count = 0
    while count < length-1:
        if yo[count][0] == yo[count+1][0]:
            a, b = yo[count][1], yo[count+1][1]
            yo[count] = (yo[count][0], a if a > b else b)
            del(yo[count+1])
            length -= 1
            continue
        count += 1

def lowest_conglomerate(myList):
    """Takes myList of the form of many (x, y) and conglomerates them by
    sorting by x, and then merging into many (x, highesht x's y).
    E.g. takes [(2, 4), (2, 3), (3, 1)] and makes it [(2,3), (3,1)]"""
    yo = myList
    yo.sort()
    length = len(yo)
    count = 0
    while count < length-1:
        if yo[count][0] == yo[count+1][0]:
            a, b = yo[count][1], yo[count+1][1]
            yo[count] = (yo[count][0], a if a < b else b)
            del(yo[count+1])
            length -= 1
            continue
        count += 1


def euler_totient(x):
    """Returns the number of numbers less than x that are relatively prime to
    x. e.g. phi(9) = 6 (1,2,4, 5, 7, 8)"""
    count = 1
    pfs = prime_factors(x)
    for num in range(2, x):
        if set(prime_factors(num)).intersection(pfs) == set([]):
            count += 1
    return(count)
        

def is_palindrome(num):
    numString = str(num)
    bar = math.floor(len(numString)/2)
    if bar == 0:
        return(True)
    for count in range(bar):
        if not numString[count] == numString[-count-1]:
            return(False)
    return(True)

def num_factors(num):
    """Returns the number of factors of num, so if num=28, returns 6
    as 28 has (1, 2, 4, 7, 14, 28) as factors"""
    x = prime_factorize(num)
    y = 1
    for thing in x:
        y *= thing[1] + 1
    return(y)

def lowest_common_multiple(numList):
    """Returns lowest common multiple of all numbers in numList"""
    megaList = []
    for num in numList:
        megaList += prime_factorize(num)
        highest_conglomerate(megaList)
    return(recombine_factors(megaList))

def highest_common_factor(numList):
    """Returns highest common factor of all numbers in numList"""
    megaList = []
    for num in numList:
        megaList.append(prime_factorize(num))

    #Gets rid of the terms that aren't common
    conglomeratedList = []
    

def find_pythagorean_triplets(maxc):
    """Returns a list of (a, b, c) where a,b,c are ints and a^2 + b^2 = c^2, and
    c <= maxc"""
    count = 1
    tripletList = []
    while count <= maxc:
        print(count, end='')
        if count % 100 == 0:
            print('')
        for a in range(1, math.floor(count/math.sqrt(2) + 1)):
            for b in range(math.ceil(count/math.sqrt(2)), count):
                if a**2 + b**2 == count**2:
                    tripletList.append((a, b, count))
        count += 1
    return(tripletList)
    

def collatz_sequence(num):
    """collatz sequence - start with positive integer. If it's even, next term
    is n/2, otherwise (3n + 1). 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1.
    Always ends in 1. This will return [num, n2, n3, n4, ... , 1]
    """
    foo = [num]
    temp = num
    while temp != 1:
        if temp % 2 == 0:
            temp = int(temp/2)
        else:
            temp = 3*temp + 1
        foo.append(temp)
    return(foo)

def geometric_progression(a, r, n):
    """Returns a list [a, ar, ar^2, ar^3, ... , ar^(n-1)]"""
    comp = []
    for num in range(n):
        comp.append(a*math.pow(r, num))
    return(comp)



def listMinus(x, y, delete=False):
    """If delete = True, removes all things in y that are in x. e.g.
    x = [1,2,3,4], y = [2,4] at the end x becomes [1,3], y remains the same.
    If delete = False, returns what x would have been while preserving x."""
    if delete == True:
        to_be_diminished = x
    else:
        to_be_diminished = x.copy()

    for thing in y:
        try:
            to_be_diminished.remove(thing)
        except ValueError:
            pass

    if delete == False:
        return(to_be_diminished)
    

def recurring_fraction_repeat_length(nominator, denominator):
    """Takes a fraction like 1/6, and returns 1 as 1/6 = 0.16666666.
    Takes 1/7 and returns 6 as 1/7 = 0.148257148257."""
    a = highest_common_factor([nominator, denominator])
    nominator = int(nominator/a)
    denominator = int(denominator/a)
    length = 1
    while True:
        pass
    
        
def sign(x):
    # If sign is positive, return True, otherwise return False
    return(abs(x) == x)

def significant_bounds(x, y):
    # Returns the number of significant figures a number between x and y is certain to.
    # e.g. x=423, y=424, returns 2
    return(1 + order_of_magnitude(y-x))



def order_of_magnitude(x):
    """Returns the nearest power of 10 less than x
    x = 0.00345, returns -3, x = 4320.0 returns 3.
    x = 5.42e+25, returns 25
    """
    stringx = str(float(x))

    # if x is in e form, just return the e multiplier
    eindex = stringx.find('e')
    if not eindex == -1:
        return(int(stringx[eindex+2:]))

    
    point_index = stringx.find('.')
    count = 0
    triggered = 0
    while True:
        #If number is like 0.0032, we skip 0s, count goes up to 4 then breaks
        if stringx[count] == '0':
            count += 1
            continue
        #For point_index - count - 1 to still work, aka 1-4-1 = -4 to be correct, 
        elif stringx[count] == '.':
            count += 1
            triggered = 1
            continue
        # If is a number like 423.55, immediately break, count is still 0, return point_index - count - 1, so here
        # It would be 2
        else:
            break
    
    return(point_index - count - 1 + triggered)
        
    


    
  
    
