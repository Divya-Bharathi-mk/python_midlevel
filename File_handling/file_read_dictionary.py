import csv
result=[]
with open("data.csv","r") as fp:
    line=csv.DictReader(fp)
    for clean in line:
        result.append((clean["first_name"],clean["gender"]))
    print(result)


    