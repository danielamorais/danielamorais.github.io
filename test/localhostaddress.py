import os

filesNameList = []

def checkFile(pathname):
    with open(pathname, "r") as ins:
        cont = 0
        for line in ins:
            cont += 1
            if "localhost:2368" in line:
                print "The file " + pathname + " contains localhost in " + str(cont) + " line"


# Open temp file in ./test and return to /static
with open("output", "r") as ins:
    filesNameList = []
    for line in ins:
        filesNameList.append(line)

# Check one file per time
for i in range(len(filesNameList)):
    if filesNameList[i].count("/") == 1:
        filesNameList[i] = filesNameList[i].replace("./", "").replace("\n", "")
        pathname = os.path.join("..", filesNameList[i])
        checkFile(pathname)
    else:
        filesNameList[i] = filesNameList[i].replace("\n", "")
        pathname = os.path.join("." + filesNameList[i])
        checkFile(pathname)

