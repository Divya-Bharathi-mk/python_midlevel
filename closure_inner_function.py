# A closure is a function that remembers the variables from its outer function even after the outer function has finished execution.
# What is happening internally? 1. outer() runs → creates x = 10, 2.inner() is returned, 3.Normally x should be gone 
#4. But closure remembers x, 5. So fun() still prints 10
# example 
def math():
    x=10
    def add():
        nonlocal x # nonlocal is a keyword used to modify the outer function data
        x=x+1
        return x
    return add
a=math()
print(a()) # 10+1 return 11, 11 values is in memory of inner class even the outer class executed
print(a()) # 11 + 1 return 12
print(a()) # 12 + 1 return 13
print(a()) # 13 + 1 return 14

#Real-Time Use Cases

#Closures are used in:

# 1. Data hiding
#Protect variables from outside access
#2. Decorators (VERY IMPORTANT)
#Logging
#Authentication
#Validation
# 3. Maintaining state
#Counters
#Caching
#Sessions
# Key Properties of Closure

#A closure must have:

#Inner function
# Outer function
# Inner uses outer variable
# Outer returns inner