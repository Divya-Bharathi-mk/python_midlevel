def decorator():
    def function(func):
        def wrapper():
            #print("Login the page")
            result=func()
            return result if result is None else ""
        return wrapper
    return function

@decorator()
def func():
    """Function name document"""
    #print("Display dashboard")

result=func()
print("Function name is",func.__name__)
print("Function document is",func.__doc__)
print("Function Object",func)