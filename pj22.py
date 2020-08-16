# -*- coding: utf-8 -*-
"""
Created on Tue Jul 12 21:45:21 2016

@author: benjamin
"""
def letter_score(name):
    letter_score = 0
    for char in name:
        letter_score += alphabet.find(char) + 1
    return(letter_score)

a = open('C:\\Users\\benjamin\\Documents\\python\\pj22_names.txt','r')
b = a.read()
c = b.split('","')

# The first element is "Name, and the last Name", so...
c[0] = c[0][1:]
c[-1] = c[-1][:-1]


c.sort()
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
score_list = []
for num in range(len(c)):
    name = c[num] 
    foo = letter_score(name)
    score_list.append([name, foo * (num+1)])

score_list.sort(key=lambda x: x[1])

