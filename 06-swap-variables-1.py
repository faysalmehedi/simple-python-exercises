# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 13:55:36 2020

@author: Faysal
"""

# This program will swap two vaiables without making temp

x = int(input("Please enter the first value x: "))
y = int(input("Please enter the second value y: "))


x, y = y, x

print(f"The value of x after swapping: {x}")
print(f"The value of y after swapping: {y}")