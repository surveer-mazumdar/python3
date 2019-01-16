#understanding of variable inside a class


class Problem4:
    __privateVar = "Some value"
    publicVar = "Some public value"

    __someConst = "Constants"

    def __init__(self):
        self.publicConstructVar = "Initialized from constructor"

    def setPrivateVar(self, value):
        self.__privateVar = value

    def getPrivateVar(self):
        return self.__privateVar

    def setPublicVar(self, value):
        self.publicVar = value

    def getPublicVar(self):
        return self.publicVar

    def setConstant(self, value):
        Problem4.__someConst = value

    def printAll(self):
        print(self.__privateVar, self.publicVar, self.publicConstructVar, Problem4.__someConst)


obj1 = Problem4()
obj2 = Problem4()

obj1.printAll()
obj2.printAll()

obj2.setPrivateVar("Some new value in private var")
obj2.setPublicVar("obj2 public var")
obj2.setConstant("obj2 const modified")

obj1.printAll()
obj2.printAll()