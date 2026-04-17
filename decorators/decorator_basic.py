# A decorator is a function that modifies or extends another function’s behavior without changing its code

def decorator_fun(fundc):
    def wrapper():
        print("Good morning")
        result=fundc()
        print("Good evening")
    return wrapper

def self():
    print("Good noon")

self=decorator_fun(self) # important syntax of decorator insdent of this we can use @ used to define the decorator
print(self())
