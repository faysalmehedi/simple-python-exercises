# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 14:36:18 2020

@author: Faysal
"""

# This program will calculate miles to kilometers conversion

miles = float(input("Please Enter miles: "))

# Conversion factors

factor = 0.621371

kilometers = miles / factor

print(f"{miles:0.2f}miles is equal to {kilometers:0.2f}km.")