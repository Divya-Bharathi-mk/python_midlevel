from functools import reduce
data=(1,2,3,4,5,6,7,8,9,10)
total=reduce(lambda x,y:x+y,[x+2 for x in data if x%2==0])
#total=[x*2 for x in data if x%2==0] list comprehension
print(total)