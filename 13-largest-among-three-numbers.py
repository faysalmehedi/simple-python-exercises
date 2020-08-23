# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 18:15:30 2020

@author: Faysal
"""

input01 = float(input("Please Enter First Number: "))
input02 = float(input("Please Enter Second Number: "))
input03 = float(input("Please Enter Third Number: "))

def check_Max_Number(num1, num2, num3):
    if (num1 >= num2) and (num1 >= num3):
        return num1
    elif (num2 >= num1) and (num2 >= num3):
        return num2
    return num3

print(f"{check_Max_Number(input01, input02, input03)} is the largest number.")
