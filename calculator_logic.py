def add(a, b):
    return a + b


def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b
    
def divide(a, b):
<<<<<<< HEAD
    if b == 0:
        raise ZeroDivisionError
    else:
        return a/b

def square(x):
    if isinstance (x, (int, float)):
        return x**2
       
    else:
         raise  ValueError                


=======
    if b != 0:
        return a / b
    else:
        return "Error"
    
>>>>>>> origin/main
