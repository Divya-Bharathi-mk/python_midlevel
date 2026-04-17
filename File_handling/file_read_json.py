import json
with open("data.json","r") as fp:
    line=json.load(fp)
    for clean in line:
        print("ID : ",clean["id"],"NAME : ",clean["first_name"])
        print("==========================================")