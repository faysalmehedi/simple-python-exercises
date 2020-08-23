# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 23:36:35 2020

@author: Faysal
"""

input01 = int(input("Please enter a number to see the multiplication table: "))

def multiplication_table(value):
    for i in range(1, 21):
        print(f"{value} X {i} = {value * i}")

multiplication_table(input01)