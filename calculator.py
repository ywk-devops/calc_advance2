import math
# Define our function
def calculate():
    operation = input('''
Please type in the math operation you would like to complete:
+ for addition
- for subtraction
* for multiplication
/ for division
cos for cosine
sin for sine
tan for tangent
''')

    number_1 = int(input('Please enter the first number: '))
    if operation != 'cos' and operation != 'sin' and operation != 'tan':
        number_2 = int(input('Please enter the second number: '))

    if operation == '+':
        print('{} + {} = '.format(number_1, number_2))
        print(number_1 + number_2)

    elif operation == '-':
        print('{} - {} = '.format(number_1, number_2))
        print(number_1 - number_2)

    elif operation == '*':
        print('{} * {} = '.format(number_1, number_2))
        print(number_1 * number_2)

    elif operation == '/':
        print('{} / {} = '.format(number_1, number_2))
        print(number_1 / number_2)

    elif operation == 'cos':
        print('cos({}) = '.format(number_1))
        print(math.cos(math.radians(number_1)))

    elif operation == 'sin':
        print('sin({}) = '.format(number_1))
        print(math.sin(math.radians(number_1)))

    elif operation == 'tan':
        print('tan({}) = '.format(number_1))
        print(math.tan(math.radians(number_1)))        

    else:
        print('You have not typed a valid operator, please run the program again.')

    again()
... 
# Define again() function to ask user if they want to use the calculator again
def again():

    # Take input from user
    calc_again = input('''
Do you want to calculate again?
Please type Y for YES or N for NO.
''')

    # If user types Y, run the calculate() function
    if calc_again == 'Y':
        calculate()

    # If user types N, say good-bye to the user and end the program
    elif calc_again == 'N':
        print('See you later.')

    # If user types another key, run the function again
    else:
        again()


# Call calculate() outside of the function  (enable after testing)
# calculate()