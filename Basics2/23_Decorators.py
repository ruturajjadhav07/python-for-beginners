# Decorators

"""
A decorator is a function that adds extra functionality to another function
WITHOUT changing its original code.

In simple words:
Decorator = Function that modifies another function.
"""

# ---------------------------------------------------
# 1. Basic Function (No Decorator)
# ---------------------------------------------------

def greet():
    print("Hello!")

greet()

# ---------------------------------------------------
# 2. Function inside Function
# ---------------------------------------------------

def outer_function():
    print("Outer Function")

    def inner_function():
        print("Inner Function")

    inner_function()

outer_function()

# ---------------------------------------------------
# 3. Function Returning Another Function
# ---------------------------------------------------

def outer():
    def inner():
        print("Inner Function Returned")
    return inner

func = outer()
func()

# ---------------------------------------------------
# 4. Simple Decorator (Without @ syntax)
# ---------------------------------------------------

def decorator(func):

    def wrapper():
        print("Before function execution")
        func()
        print("After function execution")

    return wrapper


def say_hello():
    print("Hello World")

# applying decorator manually
decorated_function = decorator(say_hello)

decorated_function()

# ---------------------------------------------------
# 5. Decorator using @ syntax
# ---------------------------------------------------

def decorator(func):

    def wrapper():
        print("Start")
        func()
        print("End")

    return wrapper

@decorator
def display():
    print("This is decorated function")

display()

# ---------------------------------------------------
# 6. Decorator with Arguments
# ---------------------------------------------------

def smart_divide(func):

    def wrapper(a, b):
        print(f"Trying to divide {a} by {b}")

        if b == 0:
            print("Error: Cannot divide by zero")
            return

        return func(a, b)

    return wrapper

@smart_divide
def divide(a, b):
    print("Result:", a / b)

divide(10, 2)
divide(10, 0)

# ---------------------------------------------------
# 7. Real Life Example (Login Check)
# ---------------------------------------------------

def login_required(func):

    def wrapper():
        print("Checking user login...")

        # suppose user is logged in
        logged_in = True

        if logged_in:
            func()
        else:
            print("Access Denied")

    return wrapper

@login_required
def dashboard():
    print("Welcome to Dashboard")

dashboard()