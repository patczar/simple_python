def say_hello(name):
    return f'Hello {name}'

def factorial(n):
    result = 1
    for i in range(1, n):
        result *= i
    return result
