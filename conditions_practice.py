#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 26 16:21:57 2024

@author: seanmilligan
"""

#import packages
import os
# Set up the exercise
#from learntools.core import binder
#binder.bind(globals())
#from learntools.intro_to_programming.ex3 import *
#from learntools.intro_to_programming.ex4q5 import excess_sugar, excess_saturated_fat, excess_trans_fat, excess_sodium, excess_calories

#check initial directory
print(os.getcwd())

#change directory
desktop_path = os.path.expanduser("/Users/seanmilligan/Desktop/Python/kaggle/practice")
os.chdir(desktop_path)

#check new directory
print(os.getcwd())

#Question 1
#grade calculation
def get_grade(score):
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 60:
        grade = "D"
    else:
        grade = "F"
    return grade

#Question 2
#cost of project redux
def cost_of_projects(engraving, solid_gold):
    if solid_gold:
        cost = 100 + 10 * engraving
    else:
        cost = 50 + 7 * engraving
    return cost

#Question 3
#cost of water bills
def get_water_bill(num_gallons):
    if num_gallons <= 8000:
        ppg = 5
    elif num_gallons <=22000:
        ppg = 6
    elif num_gallons <= 30000:
        ppg = 7
    elif num_gallons > 30000:
        ppg = 10
    return ppg * (num_gallons / 1000)
get_water_bill(22001)

#Question 4
#data services
def get_phone_bill(gb):
    if gb <= 15:
        bill = 100
    else:
        bill = 100 + ((gb - 15) * 100)
    return bill
get_phone_bill(15.5)

#Question 5
#mexican foods
def get_labels(food_type, serving_size, calories_per_serving, saturated_fat_g, trans_fat_g, sodium_mg, sugars_g):
    # Print messages based on findings
    if excess_sugar(sugars_g, calories_per_serving) == True:
        print("EXCESO AZÚCARES / EXCESS SUGAR")
    if excess_saturated_fat(saturated_fat_g, calories_per_serving) == True:
        print("EXCESO GRASAS SATURADAS / EXCESS SATURATED FAT")
    if excess_trans_fat(trans_fat_g, calories_per_serving) == True:
        print("EXCESO GRASAS TRANS / EXCESS TRANS FAT")
    if excess_sodium(calories_per_serving, sodium_mg) == True:
        print("EXCESO SODIO / EXCESS SODIUM")
    if excess_calories(food_type, calories_per_serving, serving_size) == True:
        print("EXCESO CALORÍAS / EXCESS CALORIES")

get_labels("solid", 32, 110, 2.5, 0, 400, 1)





