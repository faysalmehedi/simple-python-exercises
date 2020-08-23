# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 14:23:00 2020

@author: Faysal
"""

# This program will generate any value between given numbers

import random

input01 = int(input("Enter a number for startpoint: "))
input02 = int(input("Enter a number for endpoint: "))

print(random.randint(input01, input02))