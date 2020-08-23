# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 14:14:11 2020

@author: Faysal
"""

x = int(input("Please enter the first value x: "))
y = int(input("Please enter the second value y: "))

# by addition and substrstraction

x = x + y
y = x - y
x = x - y

print("This swapping variable used addition and substraction")
print(f"The value of x after swapping: {x}")
print(f"The value of y after swapping: {y}")

x = x * y
y = x / y
x = x / y

print("This swapping variable used Multiplication and division")
print(f"The value of x after swapping: {x}")
print(f"The value of y after swapping: {y}")


# Reminder: XOR operator will only work with integers

x = int(x) 
y = int(y)
x = x ^ y
y = x ^ y
x = x ^ y

print("This swapping variable used XOR swap")
print(f"The value of x after swapping: {x}")
print(f"The value of y after swapping: {y}")