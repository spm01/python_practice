#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 21:26:22 2024

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

#organizing code with functions
#define given function
def add_three(input_var):
    output_var = input_var + 3
    return output_var

#run a function by 'calling' it
new_number = add_three(10)
print(new_number)

def get_pay(num_hours):
    #pre-tax pay, based on $15/hour
    pay_pretax = num_hours * 15
    #after-tax pay, based on 12% tax
    pay_aftertax = pay_pretax * (1 - 0.12)
    return pay_aftertax

pay_fulltime = get_pay(40)
print(pay_fulltime)

pay_parttime = get_pay(32)
print(pay_parttime)

#more complicated function
def get_pay_with_more_inputs(num_hours, hourly_wage, tax_bracket):
    #pre-tax pay
    pay_pretax = num_hours * hourly_wage
    #after-tax pay
    pay_aftertax = pay_pretax * (1 - tax_bracket)
    return pay_aftertax

#to get output, must provide input separated by commas
higher_pay_aftertax = get_pay_with_more_inputs(40, 24, 0.22)
print(higher_pay_aftertax)

#can get original output with complex function too
same_pay_fulltime = get_pay_with_more_inputs(40, 15, 0.12)
print(same_pay_fulltime)

#can define functions without arguments
def print_hello():
    print('Hello, you!')
    print('Good morning!')
print_hello()







