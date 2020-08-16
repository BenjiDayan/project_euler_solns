#!/usr/bin/python3

import math
import tqdm

def is_palindrome(num):
    num_list = [int(x) for x in str(num)]
    length = math.floor(len(num_list)/2)
    temp = num_list[:length].copy()
    num_list.reverse()
    return(num_list[:length] == temp)

comp = []
for num in tqdm.tqdm(range(1, 10000)):
    for _ in range(50):
        reversed_num = [x for x in str(num)]
        reversed_num.reverse()
        reversed_num = int(''.join(reversed_num))
        num += reversed_num
        if is_palindrome(num):
            comp.append(num)
            break

print("there are {} lychrel numbers below 10000".format(10000 - 1 - len(comp)))
    

