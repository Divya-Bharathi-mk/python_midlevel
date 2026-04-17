"""
================ Eligible checker=========
data=[
   { "name":"Divya","age":26,},
   {"name":"kanika","age":17}
]

adult=list(filter(lambda x:x["age"]>=18 if "eligible to vote" else "not eligible",data))
print(adult)
"""

data=[
   { "name":"Divya","age":26},
   {"name":"kanika","age":17},
   {"name": "","age":10}
]
result=list(filter(lambda x:x["name"]!="",data))
print(result)