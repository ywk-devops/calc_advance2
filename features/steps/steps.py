from behave import *
from calculator import calculate
import math

@given('I have a calculator')
def step_given_calculator(context):
    context.result = None
    context.number_1 = None
    context.number_2 = None
    context.operation = None

@when('I input {operation} as the operation')
def step_when_input_operation(context, operation):
    context.operation = operation

@when('I input {number_1:d} as the first number')
def step_when_input_first_number(context, number_1):
    context.number_1 = number_1

@when('I input {number_2:d} as the second number')
def step_when_input_second_number(context, number_2):
    context.number_2 = number_2

@then('the result should be {expected_result}')
def step_then_verify_result(context, expected_result):
    if context.operation == '+':
        context.result = context.number_1 + context.number_2
    elif context.operation == '-':
        context.result = context.number_1 - context.number_2
    elif context.operation == '*':
        context.result = context.number_1 * context.number_2
    elif context.operation == '/':
        context.result = context.number_1 / context.number_2
    elif context.operation == 'cos':
        context.result = math.cos(math.radians(context.number_1))
    elif context.operation == 'sin':
        context.result = math.sin(math.radians(context.number_1))
    elif context.operation == 'tan':
        context.result = math.tan(math.radians(context.number_1))
    else:
        raise ValueError(f"Invalid operation: {context.operation}")

    
    # Ensure the result matches expected
    if isinstance(context.result, float):
        assert math.isclose(context.result, float(expected_result), rel_tol=1e-9), \
            f"Expected {expected_result}, got {context.result}"
    else:
        assert context.result == int(expected_result), \
            f"Expected {expected_result}, got {context.result}"
