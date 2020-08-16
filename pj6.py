#pj6

import math

a = 0
b = 0
for num in range(1, 101):
    a += math.pow(num, 2)
    b += num

b = math.pow(b, 2)
print(b-a)
