"""
import csv
with open("data.csv","r") as fp:
    line=csv.reader(fp)
    data=list(line)
    print(data)
"""
import csv 
with open("data.csv","r") as fp:
    line=csv.reader(fp)
    next(line)
    for clean in line:
        print(clean)