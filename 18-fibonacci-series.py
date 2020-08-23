# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 23:45:20 2020

@author: Faysal
"""

print("This program will print fibonacci series for you. :)")

input01 = int(input("How many terms you want to see: "))

def fibonacci_series(value):
    n1, n2 = 0, 1
    count = 0

    if value <= 0:
        print("Please enter a positive number.")
    elif value == 1:
        print(f"Fibonacci sequence upto {value}: ")
        print(n1)
    else:
        print(f"Fibonacci sequence upto {value}: ")
        while count < value:
            print(n1)
            nth = n1 + n2
            # update value
            n1 = n2
            n2 = nth
            count += 1

fibonacci_series(input01)