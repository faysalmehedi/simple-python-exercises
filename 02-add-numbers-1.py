#This program will use function for ading numbers

def Add(num1, num2):
    return num1 + num2

input01 = int(input("Give me a number: "))
input02 = int(input("Give me another number: "))

sum = Add(input01, input02)

print(f"The sum of {input01} and {input02} is {sum}.")
