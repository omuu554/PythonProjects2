import os

def readFromFile(fileName):
    if(not os.path.exists(fileName)):
        raise Exception("Bad File")
    infile = open(fileName, 'r')
    line = infile.readline()
    return line
