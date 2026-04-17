# A decorator with arguments needs 3 functions
'''
outer → takes decorator arguments  
   ↓
decorator → takes function  
   ↓
wrapper → takes function arguments
'''

def decorator_args(value,name):
    def decorator_func(log):
        def wrapper(*args, **kwargs):
            print("Login the device")
            print(name)
            nonlocal value
            print(value)
            value=value + 5
            print(value)
            result=log(*args, **kwargs)
            print("Logout successfully")
            return result if result is not None else ""
        return wrapper
    return decorator_func
@decorator_args(5,name="Divya")
def log():
    print("Login successfully")

result=log()
print(result)
result1=log()
print(result1)
