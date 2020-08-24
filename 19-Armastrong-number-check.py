# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 13:43:38 2020

@author: Faysal
"""

input01 = input("Please input a number to check if this is a Armstrong Number or Not: ")

def check_Armstrong_number(value):
    count = 0
    for s in value:
        count = count + (int(s) ** len(value))
    if count == int(value):
        return f"{value} is an Armstrong number."
    else:
        return f"{value} is NOT an Armstrong number."
    
print(check_Armstrong_number(input01))



