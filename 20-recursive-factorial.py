# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 14:39:40 2020

@author: Faysal
"""
input01 = int(input("Please enter a number: "))

def factorial(x):
    """
    This is a recursive function
    to find the factorial of an integer.
    """
    
    if x == 1:
        return 1
    else:
        return (x * factorial(x-1))
    
print(f"The factorial of {input01} is {factorial(input01)}.")



