#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 21:40:42 2024

@author: seanmilligan
"""

#import packages
import os
# Set up the exercise
#from learntools.core import binder
#binder.bind(globals())
#from learntools.intro_to_programming.ex3 import *

#check initial directory
print(os.getcwd())

#change directory
desktop_path = os.path.expanduser("/Users/seanmilligan/Desktop/Python/kaggle/practice")
os.chdir(desktop_path)

#check new directory
print(os.getcwd())

#Question 1
#convert float into integer with int function
#define float
y = 1.
print(y)
print(type(y))

#convert float into integer
z = int(y)
print(z)
print(type(z))

print(int(1.2321))
print(int(1.747))
print(int(-3.94535))
print(int(-2.19774))

#Question 2
print(3 * True)
print(-3.1 * True)
print(type("abc" * False))
print(len('abc' * False))

#multiplying integer/float by True returns same integer/float
#multiply integer/float by False returns 0 (negative/positive numbers)
#multiply string by True returns same string
#multiply string by False returns empty string (length 0)

#Question 3
#estimate value of house
def get_expected_cost(beds, baths, has_basement):
    base_cost = 80000
    bed_value = beds * 30000
    bath_value = baths * 10000
    basement = has_basement * 40000
    total_cost = base_cost + bed_value + bath_value + basement
    return total_cost

#Question 4
#boolean arithmetic
print(False + False)
print(True + False)
print(False + True)
print(True + True)
print(False + True + True + True)
#adding True is equivalent to adding 1
#adding False is equivalent to adding 0

#Question 5
#online shop
def cost_of_project(engraving, solid_gold):
    cost = solid_gold * (100 + 10 * len(engraving)) + (not solid_gold) * (50 + 7 * len(engraving))
    return cost

project_one = cost_of_project("Charlie+Denver", True)
print(project_one)

project_two = cost_of_project("08/10/2000", False)
print(project_two)



