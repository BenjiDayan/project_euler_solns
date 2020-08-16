#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 12 13:33:18 2018

@author: benji
"""

import math

def is_rightangled(a, b, c):
    return (a**2 + b**2 == c**2)

patterns = [] # lowest denominator triples [[a, b, c], a+b+c] a^2 + b^2 = c^2

n = 20

rtriangles = []

for perimeter in range(1, n):
    print("### {0}".format(perimeter))
    cmin = math.ceil(perimeter/3)
    cmax = math.floor(perimeter/math.sqrt(2))
    for c in range(cmin, cmax+1):
        bmax = c-1
        for b in range(1, bmax+1):
            a = perimeter - (b + c)
            print(b, a, c)
            if is_rightangled(a, b, c):
                rtriangles.append([b, a, c])
    