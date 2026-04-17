data=[6,7,9,3,2,10]
result=sorted(map(lambda x:x*2,filter(lambda x:x%2==0,data)))
print(result)