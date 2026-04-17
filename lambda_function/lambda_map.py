"""
map() is a function that applies a function to every item in an iterable (like list, tuple, etc.)
map(function, iterable)
when we need to use ?
You want to apply the SAME operation to every item in a list (or iterable)

One function → many items → same logic
Use map() when you want to apply the same transformation to every element in a collection.

"""
"""
 ------------ With string --------
num=("kani","anni","divi","pavi")
app=sorted(list(map(lambda x:x.lower(),num)))
print(app)
"""
"""
------------ Multiple list combine-------
num=(1,2,3,5)
num1=(2,8,9,9)
app=sorted(list(map(lambda x,y:x+y,num,num1)))
print(app)
"""
num=["1","2","5","8"]
app=list(map(int,num))
print(app)
