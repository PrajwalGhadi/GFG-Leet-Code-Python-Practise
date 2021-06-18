'''Date - 11-06-2021
Author - Prajwal Ghadi
Aim - Lambda with if but without else in Python.'''

# Lambda without else will create an Error
square = lambda x: x*x if (x > 0) else None
print(square(5))

square1 = [x, lambda x: x*x if (x > 0) else None] #timepass