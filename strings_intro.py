#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  3 16:49:26 2024

@author: seanmilligan
"""

#import packages
import os

#check initial directory
print(os.getcwd())

#change directory
desktop_path = os.path.expanduser("/Users/seanmilligan/Desktop/Python/kaggle/practice")
os.chdir(desktop_path)

#check new directory
print(os.getcwd())

#string syntax
#can use both double and single quotes to create a string
x = 'Pluto is a planet'
y = "Pluto is a planet"
x == y

print("Pluto's a planet!")
print('My dog is named "Pluto"')

#using a single quote character in single quote string confuses Python
#escap the single quote with a backslash
'Pluto\'s a planet!'

#line breaks are '\n'
hello = "hello\nworld"
print(hello)

#triple syntax allows for newlines
triplequoted_hello = """hello
world"""
print(triplequoted_hello)
triplequoted_hello == hello

#strings can be treated as sequences of characcters
#indexing
planet = 'Pluto'
planet[0]
planet[-3:]

len(planet)
#can also loop over them
[char+'! ' for char in planet]
#but strings cannot be modified

#string methods
claim = "Pluto is a planet!"
claim.upper()
claim.lower()
claim.index('plan')
claim.startswith(planet)
claim.endswith('planet')

#.split() turns a string into list of smaller strings
words = claim.split()
words

#str.join() combines strings into one
datestr = '1956-01-31'
year, month, day = datestr.split('-')

'/'.join([month, day, year])

#can also build strings with .format()
planet + ', we miss you.'
position = 9
planet + ", you'll always be the " + str(position) + "th planet to me."
"{}, you'll always be the {}th planet to me.".format(planet, position)

#dictionaries are built in Python structure for mapping keys to values
numbers = {'one':1, 'two':2, 'three':3}
numbers['one']

#can add to dictionaries using same syntax
numbers['eleven'] = 11
numbers

numbers['one'] = 'Pluto'
numbers

#can use dictionary comprehensions
planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
planet_to_initial = {planet: planet[0] for planet in planets}
planet_to_initial

#'in' operator tells us whether something is a key in the dictionary
'Saturn' in planet_to_initial
'Betelgeuse' in planet_to_initial

#a for loop over a dictionary will loop over its keys
for k in numbers:
    print('{} = {}'.format(k, numbers[k]))












