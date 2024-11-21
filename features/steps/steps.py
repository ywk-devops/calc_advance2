from behave import *
from calculator import add, subtract, multiply, divide, sine, cosine, tangent

@given('the calculator is initialized')
def step_given_calculator_initialized(context):
    context.result = None

@when('I add {a:d} and {b:d}')
def step_when_add(context, a, b):
    context.result = add(a, b)

@when('I subtract {a:d} from {b:d}')
def step_when_subtract(context, a, b):
    context.result = subtract(b, a)

@when('I multiply {a:d} and {b:d}')
def step_when_multiply(context, a, b):
    context.result = multiply(a, b)

@when('I divide {a:d} by {b:d}')
def step_when_divide(context, a, b):
    try:
        context.result = divide(a, b)
    except ValueError as e:
        context.result = str(e)

@when('I calculate the sine of {angle:d}')
def step_when_sine(context, angle):
    context.result = round(sine(angle), 9)  # Rounding to avoid floating-point precision issues

@when('I calculate the cosine of {angle:d}')
def step_when_cosine(context, angle):
    context.result = round(cosine(angle), 9)

@when('I calculate the tangent of {angle:d}')
def step_when_tangent(context, angle):
    context.result = round(tangent(angle), 9)

@then('the result should be {expected_result}')
def step_then_result_should_be(context, expected_result):
    # Handle floating-point results
    if isinstance(context.result, float):
        expected_result = float(expected_result)
        assert round(context.result, 9) == round(expected_result, 9), \
            f"Expected {expected_result}, but got {context.result}"
    else:
        # Handle string and integer results
        if expected_result.isdigit():
            expected_result = int(expected_result)
        assert context.result == expected_result, \
            f"Expected {expected_result}, but got {context.result}"
