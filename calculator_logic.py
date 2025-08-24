def add(a, b):
    return a + b


def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b
    
def divide(a, b):
    if b == 0:
        raise ZeroDivisionError
    else:
        return a/b

def square(x):
    if isinstance (x, (int, float)):
        return x**2
       
    else:
         raise  ValueError                


