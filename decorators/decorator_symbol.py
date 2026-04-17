def decorator_fun(extence):
    def wrapper():
        print("I had my breakfast")
        result=extence()
        print("I had my dinner")
        return result if result is not None else ""
    return wrapper
@decorator_fun
def lunch():  # internally it will convert as 'lunch=decorator_fun(lunch)'
    print("I had my lunch")

print(lunch())