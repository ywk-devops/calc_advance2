import math

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero!"
    elif b != 0:
        return a / b
    else:
        pass
    
def sine(angle):
    return math.sin(math.radians(angle))

def cosine(angle):
    return math.cos(math.radians(angle))

def tangent(angle):
    if angle != 90 or angle != 270:
        return math.tan(math.radians(angle))
    else:
        return "90 degree is not allowed!"
        
while True:
#   operation = input("Operation (+, -, *, /, cos, sin, tan): ")
#
#   number_1 = int(input('Please enter the first number: '))
#   if operation != 'cos' and operation != 'sin' and operation != 'tan':
#       number_2 = int(input('Please enter the second number: '))

    operation = '+'
    number_1  = 10
    number_2  = 10

    if operation == '+':
        print('{} + {} = '.format(number_1, number_2))
        print(add(number_1, number_2))

    elif operation == '-':
        print('{} - {} = '.format(number_1, number_2))
        print(subtract(number_1, number_2))

    elif operation == '*':
        print('{} * {} = '.format(number_1, number_2))
        print(multiply(number_1, number_2))

    elif operation == '/':
        print('{} / {} = '.format(number_1, number_2))
        print(divide(number_1, number_2))

    elif operation == 'cos':
        print('cos({}) = '.format(number_1))
        print(cosine(number_1))

    elif operation == 'sin':
        print('sin({}) = '.format(number_1))
        print(sine(number_1))

    elif operation == 'tan':
        print('tan({}) = '.format(number_1))
        print(tangent(number_1))        

    else:
        print('You have not typed a valid operator, please run the program again.')

    # Take input from user
#   calc_again = input("Do you want to calculate again (Any key for YES or (N or n) for NO)? ")
    calc_again = 'N'

    # If user types N, say good-bye to the user and end the program
    if calc_again == 'N' or calc_again == 'n':
        print('See you later.')
        break

        