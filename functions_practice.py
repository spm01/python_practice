#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 17:10:44 2024

@author: seanmilligan
"""

#import packages
import os
import math
#from learntools.core import binder
#binder.bind(globals())
#from learntools.intro_to_programming.ex2 import *
print('Setup complete')

#check initial directory
print(os.getcwd())

#change directory
desktop_path = os.path.expanduser("/Users/seanmilligan/Desktop/Python/kaggle/practice")
os.chdir(desktop_path)

#check new directory
print(os.getcwd())

#Question 1
#create function to predict house prices
def get_expected_cost(beds, baths):
    base_cost = 80000
    beds_value = beds * 30000
    baths_value = baths * 10000
    total_value = base_cost + beds_value + baths_value
    return total_value

get_expected_cost(2, 2)

#Question 2
#use the new function to find values for new houses
option_1 = get_expected_cost(2, 3)
option_2 = get_expected_cost(3, 2)
option_3 = get_expected_cost(3, 3)
option_4 = get_expected_cost(3, 4)

print(option_1)
print(option_2)
print(option_3)
print(option_4)

#Question 3
#create a function that calculates cost of room paintings

def get_cost(sqft_walls, sqft_ceiling, sqft_per_gallon, cost_per_gallon):
    total_sqft = sqft_walls + sqft_ceiling
    gallons_needed = total_sqft / sqft_per_gallon
    cost = cost_per_gallon * gallons_needed
    return cost

#Question 4
#use the function to calculate cost of applying paint
project_cost = get_cost(432, 144, 400, 15)
print(project_cost)

#Question 5
#no longer able to buy fractions of gallons
#make new function to account for this
def get_actual_cost(sqft_walls, sqft_ceiling, sqft_per_gallon, cost_per_gallon):
    total_sqft = sqft_walls + sqft_ceiling
    gallons_needed = total_sqft / sqft_per_gallon
    true_gallons_needed = math.ceil(gallons_needed)
    cost = true_gallons_needed * cost_per_gallon
    return cost
get_actual_cost(432, 144, 400, 15)
get_actual_cost(594, 288, 400, 15)





