#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 19:20:44 2024

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

#conditions are statements of true or false
#can be simple checks or complicated functions
print(2 > 3)

#can use conditions to compare variable values
var_one = 1
var_two = 2
print(var_one < 1)
print(var_two >= var_one)

#== 	equals
#!= 	does not equal
#< 	less than
#<= 	less than or equal to
#> 	greater than
#>= 	greater than or equal to

#conditional statements use conditions to modify function performance
#if evaluated to True, then code runs
#if evaluated to False, then code stops

#If Statements -> simple form of conditional
def evaluate_temp(temp):
    message = 'Normal temperature.'
    #update value of message only if temperature greater than 38
    if temp > 38:
        message = "Fever!"
    return message
print(evaluate_temp(37))
print(evaluate_temp(39))

#two levels of indentation
#level 1: need to indent code inside block
#level 2: need to indent code for if statement

#can also use if/else statements if a code statement is False
def evaluate_temp_with_else(temp):
    if temp > 38:
        message = 'Fever!'
    else:
        message = 'Normal temperature.'
    return message

print(evaluate_temp_with_else(37))

#can use if/elif/else statements to check multiple conditions
def evaluate_temp_with_elif(temp):
    if temp > 38:
        message = 'Fever!'
    elif temp > 35:
        message = 'Normal temperature.'
    else:
        message = 'Low temperature.'
    return message

evaluate_temp_with_elif(36)
evaluate_temp_with_elif(34)

#can be used for calculations too!
def get_taxes(earnings):
    if earnings < 12000:
        tax_owed = 0.25 * earnings
    else:
        tax_owed = 0.30 * earnings
    return tax_owed

ana_taxes = get_taxes(9000)
bob_taxes = get_taxes(15000)
print(ana_taxes)
print(bob_taxes)

#sample problem
def add_three_or_eight(input):
    if input < 10:
        result = input + 3
    else:
        result = input + 8
    return result
print(add_three_or_eight(5))
print(add_three_or_eight(11))

#example of multiple elif statements
def get_dose(weight):
    if weight < 5.2:
        dose = 1.25
    elif weight < 7.9:
        dose = 2.5
    elif weight < 10.4:
        dose = 3.75
    elif weight < 15.9:
        dose = 5
    elif weight < 21.2:
        dose = 7.5
    #dosage is 10mL for anyone 21.2kg or over
    else:
        dose = 10
    return dose
print(get_dose(12))








