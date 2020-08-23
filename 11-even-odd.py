# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 14:57:27 2020

@author: Faysal
"""

input01 = int(input("Please enter a number: "))

def check_even_odd(value):
    if value % 2 == 0:
        return "This number is even."
    return "This number is odd."

print(check_even_odd(input01))