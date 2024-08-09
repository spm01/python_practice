#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 17:50:49 2024

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

#Integers -> numbers w/o fractions (1, -1, 0, etc.)
x = 14
print(x)
print(type(x))

#Floats -> numbers with fractional parts
nearly_pi = nearly_pi = 3.14
print(nearly_pi)
print(type(nearly_pi))

#can also specify floats with fractions
almost_pi = 22 / 7
print(almost_pi)
print(type(almost_pi))

#rounding is also possible
rounded_pi = round(almost_pi, 5)
print(rounded_pi)
print(type(rounded_pi))
#python will always recognize decimal points ass floats
y_float = 1.
print(y_float)
print(type(y_float))

#Booleans -> represent one of two values: True or False
z_one = True
print(z_one)
print(type(z_one))

z_two = False
print(z_two)
print(type(z_two))

z_three = (1 < 2)
print(z_three)
print(type(z_three))

z_four = (5 < 3)
print(z_four)
print(type(z_four))

z_five = not z_four 
print(z_five)
print(type(z_five))

#Strings -> collection of characters contained in quotes
#typically used to represent texts
w = 'Hello, Python!'
print(w)
print(type(w))
print(len(w))

shortest_string = ''
print(type(shortest_string))
print(len(shortest_string))

#if a number is put in quotes, it becomes a string
my_number = '1.12321'
print(my_number)
print(type(my_number))

#can convert strings to floats using 'float()'
also_my_number = float(my_number)
print(also_my_number)
print(type(also_my_number))

#can also add strings 
new_string = 'abc' + 'def'
print(new_string)
print(type(new_string))

#cannot multiply string by string but can multiply by integer
newest_string = 'abc' * 3
print(newest_string)
print(type(newest_string))











