# -*- coding: utf-8 -*-
"""
Created on Wed Jul 13 17:52:37 2016

@author: benjamin
"""
import math
import pickle

def proper_divisors(x):
    """Returns the list of proper divisors of x, numbers
    less than n which divide evenly into x."""
    comp = []
    for num in range(1, math.floor(x/2) + 1):
        if x % num == 0:
                comp.append(num)
    return(comp)
                
def list_minus(x, y):
    """removes all elements in x that are in y"""
    for thing in x:
        if thing in y:
            x.remove(thing)

def is_abundant(x):
    return(sum(proper_divisors(x)) > x)


temp = open('abundant_numbers', 'rb')
abundant_numbers = pickle.load(temp)
temp.close()

def shift(my_list):
    """my_list = [1,2,3,4]
       my_list = [4,3,2,1]"""
    my_list.insert(0, my_list[-1])
    del(my_list[-1])

def add(listx, listy):
    temp = []
    for num in range(len(listx)):
        temp.append(listx[num] + listy[num])
    return(temp)
    
#a = list(range(1, 28123))
#list_minus(a, sum_of_two_abundant_nums)


