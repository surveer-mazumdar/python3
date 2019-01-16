'''
Read a file having data like
U1, U2
U3, U4
U1, U5
U2, U1
U3, U4

Eliminate duplicates even in combination of U1, U2 and U2, U1. Result should be like

U1, U2
U3, U4
U1, U5
'''

class FileHandler:
    srcFile = "./files/problem1-src.txt"
    destFile = "./files/problem1-dest.txt"

    def __init__(self, src = "", dest=""):
        #self.srcFile = src
        #self.destFile = dest
        contents = self.__readFile()
        uniqueSet = self.__processData(contents)
        self.__writeFile(uniqueSet)

    def __readFile(self):
        fileObj = open(self.srcFile, "r")
        contents = fileObj.readlines()
        return contents

    def __processData(self, contentsList):

        uniqueSet = list()
        for line in contentsList:
            setOne = line.split(",")
            setOne = setOne[0].strip() + "," + setOne[1].strip() + '\n'

            setTwo = line.split(",")
            setTwo = setTwo[1].strip() + "," + setTwo[0].strip()+ '\n'

            if setOne not in uniqueSet and setTwo not in uniqueSet:
                uniqueSet.append(setOne)
        return uniqueSet

    def __writeFile(self, uniqueSet):

        fileObj = open(self.destFile, "w")
        fileObj.writelines(uniqueSet)
        fileObj.close()


obj = FileHandler()