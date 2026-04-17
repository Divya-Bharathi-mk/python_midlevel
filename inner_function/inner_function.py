def math():
    x=20
    y=25
    def add():
        A=x+y
        return A
    def sub():
        S=x-y
        return S
    def mul():
        M=x*y
        return M
    def div():
        D=x/y
        return D
    return add(),sub(),mul(),div() # return as tuple

fun=math()
print(fun) # Functions are callable objects, but tuples are just data containers, so they cannot be invoked.”

print(fun[0])
print(fun[1])
print(fun[3])



