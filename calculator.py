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
    if angle != 90:
        return math.tan(math.radians(angle))