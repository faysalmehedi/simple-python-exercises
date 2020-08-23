# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 14:52:42 2020

@author: Faysal
"""

input01 = int(input("Please enter a number: "))

def check_positive_negative(input01):
    if input01 == 0:
        print("This number is ZERO.")
    elif input01 > 0:
        print(f"{input01} is POSITIVE number.")
    else:
        print(f"{input01} is NEGATIVE number.")
        
check_positive_negative(input01)