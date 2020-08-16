import math
import tqdm

def p3(n):
    return(int(n*(n+1)/2))
def p4(n):
    return(int(n**2))
def p5(n):
    return(int(n*(3*n-1)/2))
def p6(n):
    return(int(n*(2*n-1)))
def p7(n):
    return(int(n*(5*n-3)/2))
def p8(n):
    return(int(n*(3*n-2)))

func_dict = {3:p3, 4:p4, 5:p5, 6:p6, 7:p7, 8:p8}
def pan(a, n):
   return(func_dict[a](n)) 


fours_dict = {key:[] for key in func_dict}
for key in fours_dict:
    i = 1
    while True:
        temp = pan(key, i)
        if temp < 1000:
            i += 1
            continue
        elif temp < 10000:
            fours_dict[key].append(temp)
            i += 1
            continue
        else:
            break


def add(previous):
    new = []
    for num_list in previous:
        used_keys = [x[1] for x in num_list]
        unused_keys = set([3,4,5,6,7,8]) - set(used_keys)
        last_num = num_list[-1][0]
        for key in unused_keys:
            usable = [x for x in fours_dict[key] if str(x)[:2] == str(last_num)[-2:]]
            for x in usable:
                new.append(num_list + [[x, key]]) 
    return(new)

tier_one = [[[x, key]] for key in fours_dict for x in fours_dict[key]]  
tiers = [tier_one]
for num in range(5):
    tiers.append(add(tiers[-1]))

ordered = []
for thing in tiers[-1]:
    order = [x[1] for x in thing]
    copy = order.copy()
    order.sort()
    if copy == order:
        ordered.append(thing)
