# This program will calculate square root for real or complex number

import cmath

# num = 1 + 2j

num = eval(input("Enter a number: "))

num_sqrt = cmath.sqrt(num)

print(f"The square root of {num} is {num_sqrt}.")
