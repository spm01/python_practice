#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 26 17:16:02 2024

@author: seanmilligan
"""
#import packages
import os
#Set up the exercise
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
#owner of a restaurant
#change menu without altering the following line
menu = ['stewed meat with onions', 'bean soup', 'risotto with trout and shrimp'
        'fish soup with cream and onion', 'gyro']

menu.remove('bean soup')
menu.append('roasted beet salad')

#Question 2
#working with customer data
num_customers = [137, 147, 135, 128, 170, 174, 165, 146, 126, 159,
                 141, 148, 132, 147, 168, 153, 170, 161, 148, 152,
                 141, 151, 131, 149, 164, 163, 143, 143, 166, 171]

avg_first_seven = (sum(num_customers[:7]) / 7)
avg_last_seven = (sum(num_customers[-7:]) / 7)
max_month = max(num_customers)
min_month = min(num_customers)

#Question 3
#string into a list
#example
flowers = "pink primrose,hard-leaved pocket orchid,canterbury bells,sweet pea,english marigold,tiger lily,moon orchid,bird of paradise,monkshood,globe thistle"
print(flowers.split(','))

#question
alphabet = "A.B.C.D.E.F.G.H.I.J.K.L.M.N.O.P.Q.R.S.T.U.V.W.X.Y.Z"
address = "Mr. H. Potter,The cupboard under the Stairs,4 Privet Drive,Little Whinging,Surrey"

letters = alphabet.split('.')
address = address.split(',')
print(letters)
print(address)

#Question 4
#list comprehensions
#create a list based on values in another list
test_ratings = [1,2,3,4,5]
#create new list where each item is boolean
test_liked = [i >= 4 for i in test_ratings]
print(test_liked)

def percentage_liked(ratings):
    list_liked = [i >= 4 for i in ratings]
    percentage_like = sum(list_liked) / len(list_liked) * 100
    return percentage_like

print(percentage_liked([1, 2, 3, 4, 5, 4, 5, 1]))

#Question 5
#percentage growth in total number of users relative to specified years ago
# TODO: Edit the function
def percentage_growth(num_users, yrs_ago):
    growth = (num_users[len(num_users)-1] - num_users[len(num_users)-yrs_ago-1])/num_users[len(num_users)-yrs_ago-1]
    return growth

# Do not change: Variable for calculating some test examples
num_users_test = [920344, 1043553, 1204334, 1458996, 1503323, 1593432, 1623463, 1843064, 1930992, 2001078]

# Do not change: Should return .036
print(percentage_growth(num_users_test, 1))

# Do not change: Should return 0.66
print(percentage_growth(num_users_test, 7)) 







