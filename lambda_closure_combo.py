#Closure means a function remembers values from where it was created
app=lambda x: (lambda y,z: x+y*z)

multi=app(10)
print(multi(2,3))
