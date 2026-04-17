"""
wraps is a function from the functools module, and while it 
- can be aliased, it is best practice to use it with its original name
"""
from functools import wraps
def decorator():
    def function(func):
        @wraps(func)
        def wrapper():
            return
        return wrapper
    return function

@decorator()
def func():
    """ Function document """
    return

result=func()
print("Function name is: ",func.__name__)
print("Function doc :", func.__doc__)
print("function object",func)
