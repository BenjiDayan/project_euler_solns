#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  8 19:52:14 2018

@author: benji
"""

# Demo file for Spyder Tutorial
# Hans Fangohr, University of Southampton, UK
import pandas as pd

def hello():
    """Print "Hello World" and return None"""
    print("Hello World")

# main program starts here


def bye():
    "Print goodbye, return NOne"
    print('goodbye')
    print('idk')


hello()
print('hi')
print('this is weird')

city_names = pd.Series(['San Francisco', 'San Jose', 'Sacramento'])
population = pd.Series([852469, 1015785, 485199])

cities = pd.DataFrame({"City name": city_names, "Population": population})
cities['Area square miles'] = pd.Series([46.87, 176.53, 97.92])
cities['Population density'] = cities['Population'] / cities['Area square miles']

cities['Is big and saintly'] = (cities['Area square miles'] > 50) & cities['City name'].apply(lambda name: name.startswith('San'))
       