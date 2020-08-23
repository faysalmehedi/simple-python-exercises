# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 15:08:58 2020

@author: Faysal
"""

input01 = int(input("Please enter a year to check if it is leap year: "))

def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return f"{year} is LEAP year."
            return f"{year} is not LEAP year."
        return f"{year} is LEAP year."
    return f"{year} is not LEAP year."
                

print(is_leap_year(input01))