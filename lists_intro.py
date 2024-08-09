#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 26 16:48:48 2024

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

#can organize names into a string
flowers = 'pink primrose, hard-leaved pocket orchid, canterbury bells, sweet pea, english marigold, tiger lily, moon orchid, bird of paradise, monkshood, globe thistle'
print(type(flowers))
print(flowers)

#can also represetn same data in a LIST
#need to use square brakcets and commas
flowers_list = ['pink primrose', 'hard-leaved pocket orchid', 'canterbury bells',
                'sweet pea', 'english marigold', 'tiger lily', 'moon orchid',
                'bird of paradise', 'monkshood', 'globe thistle']
print(type(flowers_list))
print(flowers_list)

#can count list entries with lists
print(len(flowers_list))

print("First entry:", flowers_list[0])
print("Second entry:", flowers_list[1])
print('Last entry:', flowers_list[9])

#can also pull a segment from the list
#called slicing 
#first x entires: [:x]
#first y entries: [:y
print('First three entries:', flowers_list[:3])
print('Final two entries:', flowers_list[-2:])

#can also remove items with .remove()
flowers_list.remove('globe thistle')
print(flowers_list)

#can add item to list using .append()
flowers_list.append('snapdragon')
print(flowers_list)

#lists can use other data types too!
hardcover_sales = [139, 128, 172, 139, 191, 168, 170]

#can get length, pull entires, and extend the list
print("Length of the list:", len(hardcover_sales))
print("Entry at index 2:", hardcover_sales[2])

#can also find the minimum and maximum values
print("Minimum:", min(hardcover_sales))
print("Maximum:", max(hardcover_sales))

#can add every item in the list
print("Total books sold in one week:", sum(hardcover_sales))

#can also do similar calculations with slices of the list
print("Average books sold in first five days:", sum(hardcover_sales[:5]) / 5)












