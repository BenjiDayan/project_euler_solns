#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 12:49:05 2018

@author: benji
"""

#[13, 5197, 5701, 6733, 8389]

import mathstuff
import tqdm
import time

def prime_pali_pair(p, q): 
    """Returns True if "pq" and "qp" are both prime"""
    a = int(str(p) + str(q))
    b = int(str(q) + str(p))
    return(mathstuff.prime(a) and mathstuff.prime(b))
    

def fits(good_list, new_prime):
    """Sees if the new_prime is a prime_pali_pair with each of the nums in good_list"""
    for num in good_list:
        if not prime_pali_pair(num, new_prime):
            return(False)
    return(True)
    
def bigger_fits(good_lists, new_prime):
    for i in range(len(good_lists)):
        if fits(good_lists[i], new_prime):
            good_lists.append(good_lists[i] + [new_prime])
    

def dumb_search(n, startn=2, good_lists=[]):
    
    #for i in tqdm.tqdm(range(2, n)):
    for i in range(startn, n+1):
        if mathstuff.prime(i):
            bigger_fits(good_lists, i)
            good_lists.append([i])
    return(good_lists)
    

def better_search(n, startn=2, good_lists=[], prime_dict={}, primes=[]):
    #primes = [] # just a list of primes we've come across, [2, 3, 5, 7, ...]
    # prime_dict's end values all point to lists in good_lists
    #good_lists = []
    #prime_dict = {}

    for i in range(startn, n+1):
        if mathstuff.prime(i):
            pali_pair_primes = [p for p in primes if prime_pali_pair(p, i)]
            for p in pali_pair_primes:
                pstuff = prime_dict[p]
                for grp in pstuff:
                    if type(grp[-1]) is list:
                        grp[-1][0] += 1
                    else:
                        grp.append([1])
            
            new_lists = [] # will add all of this to good_lists at the end
            prime_dict[i] = [] # new prime
            for good_list in good_lists:
                # If our new prime matched with all of it, add new_list to prime_dict and new_lists
                if good_list[-1] == [len(good_list) - 1]:
                    new_list = good_list.copy()[:-1] + [i]
                    new_lists.append(new_list)
                    
                    # update prime_dict
                    for old_prime in good_list[:-1]:
                        prime_dict[old_prime].append(new_list)
                    prime_dict[i].append(new_list)
                        
                # clean up good_list
                if type(good_list[-1]) is list:
                    good_list.pop(-1)
                
            # update good_lists
            good_lists += new_lists
            singlet = [i]
            good_lists.append(singlet)
            prime_dict[i].append(singlet)
            
            primes.append(i)
            
    return([good_lists, prime_dict, primes])
            
    
#qwert = better_search(50)
#qwert2 = dumb_search(50)

def temp_timer(n):
    time1 = time.time()
    a = better_search(n)
    time1 = time.time()-time1
    
    time2 = time.time()
    b = dumb_search(n)
    time2 = time.time()-time2
    return([time1, time2])
    
def temp_timer2(n, num_intervals):
    startpoints = list(range(2, n, int((n-2)/num_intervals)))
    startpoints.append(n+1)
    a, b = [[], {}, []], []
    times = [[0], [0]]
    for i in range(len(startpoints) - 1):
        startn, endn = startpoints[i], startpoints[i+1]-1
        time1 = time.time()
        a = better_search(endn, startn, a[0], a[1], a[2])
        times[0].append(times[0][-1] + time.time() - time1)
        
#        time2 = time.time()
#        b = dumb_search(endn, startn, b)
#        times[1].append(times[1][-1] + time.time() - time2)
        
    return([a, b, times])
        
        