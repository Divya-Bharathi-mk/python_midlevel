with open("data.txt","w") as fp:
    result=fp.write("hello world\nhello mammy\n poda mama")
    print(result) # write is used to over write the data
with open("data.txt","r") as fp:
    result=fp.read()
    print(result)