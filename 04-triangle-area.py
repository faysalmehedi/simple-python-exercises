# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 15:07:37 2020

@author: Faysal
"""

# This program will calculate the area of a triangle

in01 = float(input("Enter first side: "))
in02 = float(input("Enter second side: "))
in03 = float(input("Enter third side: "))

# calculate the semi-perimeter

def calculate_area_of_triangle(first_side, second_side, third_side):

    semi_perimeter = (first_side + second_side + third_side) / 2

    area = (semi_perimeter * (semi_perimeter - first_side) * (semi_perimeter - second_side) * (semi_perimeter - third_side)) ** 0.5

    return area

area = calculate_area_of_triangle(in01, in02, in03)

# print("The area of triangle is {:0.3f}".format(area)) 
print(f"The area of triangle is {area:0.3f}")