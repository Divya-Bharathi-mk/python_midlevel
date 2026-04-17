with open("data.txt") as fp:
    line=[line.strip().upper() for line in fp]
with open("data.txt","w") as fp:
    for clean in line:
        fp.write(clean + "\n")
    print("File updated")