with open("404.html", "r") as ins:
    contains = None
    cont = 0  
    for line in ins:
        cont += 1
        if "localhost:2368" in line:
            contains = True
            print cont
    print contains
