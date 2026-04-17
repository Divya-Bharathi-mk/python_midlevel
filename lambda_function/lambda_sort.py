data=[("apple",2),("kiwi",1),("dragon fruit",3)]
data1=("kavi","pavi","Divi")
data2=[
    {
        "id":2,"name":"kani"
        },
        {
            "id":1,"name":"divi"
        }
    ]
sort=sorted(data, key=lambda x:x[0])
print(sort)
sort1=sorted(data,key=lambda x:x[1])
print(sort1)
sort2=sorted(data1,key=lambda x:x.lower())
print(sort2)
sort3=sorted(data2,key=lambda x:x["name"])
print(sort3)
sort4=sorted(data2,key=lambda x:x["id"])
print(sort4)