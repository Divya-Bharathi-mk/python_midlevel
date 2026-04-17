def decorator1():
    def function1(func):
        def wrapper1():
            print("before - 1")
            result=func()
            print("after - 1")
            return result if result is not None else " "
        return wrapper1
    return function1
def decorator2():
    def function2(func):
        def wrapper2():
            print ("before - 2")
            result=func()
            print("after - 2")
            return result if result is not None else " "
        return wrapper2
    return function2

@decorator1()
@decorator2()
def func():
    print("Dashboard")

func()
