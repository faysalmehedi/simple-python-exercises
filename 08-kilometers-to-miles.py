# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 14:29:22 2020

@author: Faysal
"""
# This program will calculate kilometers to miles conversion

kilometers = float(input("Please Enter kilometers: "))

# Conversion factors
factor = 0.621371

miles = kilometers * factor

print(f"{kilometers:0.2f}km is equal to {miles:0.2f}miles.")
