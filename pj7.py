#pj7

import mathStuff

primeList = []
count = 0
num_count = 1
while count < 10001:
    while True:
        num_count += 1
        if not mathStuff.not_prime(num_count):
            primeList.append(num_count)
            break
    count += 1


            
