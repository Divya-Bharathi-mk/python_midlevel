import csv
value=[
    ["id","first_name","last_name","email","gender","ip_address"],
    [15,"Divya","Manikaran","emailid@gmain.com","6e569896wef"]
       ]
with open("data.csv","w",newline="") as fp:
    line=csv.writer(fp)
    data=line.writerows(value)
print("File updated")


