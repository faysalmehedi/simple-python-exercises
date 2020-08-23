# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 19:03:01 2020

@author: Faysal
"""
print("Listing PRIME numbers.")
input01 = int(input("Enter a lower number: "))
input02 = int(input("Enter a upper number: "))

prime_numbers = []

def is_prime_list(lower, upper):
    for num in range(lower, upper + 1):    
        if num > 1:
            for i in range(2, num // 2):
                if num % i == 0:
                    break
            else:
                prime_numbers.append(num)
    return prime_numbers

print(is_prime_list(input01, input02))