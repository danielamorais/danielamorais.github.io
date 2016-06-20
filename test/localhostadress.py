filesName = []

with open("output", "r") as ins:
    filesNamey = []
    for line in ins:
        filesName.append(line)
    
for i in filesName:
    print filesName[i]

