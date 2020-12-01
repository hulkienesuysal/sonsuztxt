liste = 0
while True:
    liste += 1
    print(liste)
    file = open("{}.txt".format(liste),"w")
    file.write("{}".format(liste))

