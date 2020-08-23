# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 23:17:01 2020

@author: Faysal
"""

input01 = int(input("Enter a number: "))

def factorial(value):
    if value < 0:
        return "not valid"
    elif value == 0:
        return "1"
    else: 
        factorial = 1

        for i in range(1, value + 1):
            factorial = factorial * i

    return factorial

print(f"The factorial of {input01} is {factorial(input01)}.")
