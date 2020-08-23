# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 18:33:58 2020

@author: Faysal
"""

input01 = int(input("Checking PRIME number or not; Enter a number: "))

def is_prime(value):
    if value < 2:
        return "Prime factors are those numbers with only two factors: 1 and themselves, and because of this, the numbers 0 and 1 cannot be prime numbers."
    for i in range(2, value//2):
        if value % i == 0:
            return f"{value} is a NOT PRIME number; {i} times {int(value / i)} is {value}."
    return f"{value} is a PRIME number."

print(is_prime(input01))
        