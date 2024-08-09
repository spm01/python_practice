#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  3 17:16:10 2024

@author: seanmilligan
"""

#import packages
import os
#Set up the exercise
from learntools.core import binder; binder.bind(globals())
from learntools.python.ex6 import *
print('Setup complete.')

#check initial directory
print(os.getcwd())

#change directory
desktop_path = os.path.expanduser("/Users/seanmilligan/Desktop/Python/kaggle/practice")
os.chdir(desktop_path)

#check new directory
print(os.getcwd())

def is_valid_zip(zip_code):
    """ Returns if input string is valid (5 digit) zip code
    """
    pass






