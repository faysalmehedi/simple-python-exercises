# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 15:08:26 2020

@author: Faysal
"""

"""
The standard form of a quadratic equation is:
ax2 + bx + c = 0, where
a, b and c are real numbers and
a ≠ 0
"""

# this program will calculate quadratic equation

import cmath

a = 1
b = 5
c = 6

# calculate the discriminant
d = (b ** 2) - (4 * a * c)

# find two solutions

sol1 = (-b - cmath.sqrt(d))/(2 * a)
sol2 = (-b + cmath.sqrt(d))/(2 * a)

print("The solution are {0} and {1}.".format(sol1, sol2))