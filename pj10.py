#pj10
from pj_euler import mathStuff

"""The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million."""

primeList = []
count = 2
while count < 2000000:
    if count % 10000 == 0:
        print(str(count) + ',', end='')
    if not mathStuff.not_prime(count):
        primeList.append(count)
    count += 1
print('')
print(sum(primeList))
    
