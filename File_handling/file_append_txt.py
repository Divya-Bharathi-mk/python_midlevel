"""
APPEND
========
Key Points (Interview Focus)
"a" never deletes existing data
If file does not exist, "a" will create it
Data is always written at the end of file
"""
with open("data.txt","a") as fp:
    result=fp.write("Hello machi\n when u came")
    print(result)
with open("data.txt","r") as fp:
    result=fp.read()
    print(result)
