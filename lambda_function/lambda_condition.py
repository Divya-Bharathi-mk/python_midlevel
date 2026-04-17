#This is list comprehension (loop) and conditional lambda
#conditional lambda =>app=lambda x: (lambda y :f"The {x+y} is Even" if (x+y)%2==0  else f"The {x+y} is ODD")
app=lambda x: (lambda y:[x+i if i%2==0 else x-i for i in range(y+1)])
multi=app(10)
print(multi(5))
