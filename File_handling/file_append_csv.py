import csv
values=[
    ["id","first_name","last_name","email","gender","ip_address"],
    [15,"Divya","manikaran","emailid@gmail.com","female","126re85985"]
        ]
with open("data.csv","a",newline="") as fp:
    data=csv.writer(fp)
    result=data.writerows(values)
print("file updated successfully")
