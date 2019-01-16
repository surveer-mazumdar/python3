#https://practice.geeksforgeeks.org/problems/pair-with-given-sum-in-a-sorted-array/0
#Pair with given sum in a sorted array
class Problem2:

    __inputArray = list()
    __sumValue = 0
    __setOfValues = list()

    def __init__(self):
        self._takeInput()
        self.__findCombination()
        self.__printFoundSets()

    def _takeInput(self):

        inputVar = ""

        while(inputVar != 'end'):
            inputVar = input('Enter element to an Array -> ');
            if (inputVar.isdigit()):
                self.__inputArray.append(int(inputVar))


        while(self.__sumValue <= 0):
            inputVar = input('Please enter Sum value. -> ')
            if (inputVar.isdigit()):
                self.__sumValue = int(inputVar)

    def __findCombination(self):
        for element in self.__inputArray:
            difference = self.__sumValue - element
            if difference >= 0:
                if difference in self.__inputArray and difference != element:
                    setFound = str(element) +" + "+ str(difference)
                    self.__setOfValues.append(setFound)

        self.__eliminateDuplicates()

    def __eliminateDuplicates(self):
        # keep one in either 7 + 1, 1 + 7
        uniqueSet = list()
        for line in self.__setOfValues:
            setOne = line.split("+")
            setOne = setOne[0].strip() + " + " + setOne[1].strip() + '\n'

            setTwo = line.split("+")
            setTwo = setTwo[1].strip() + " + " + setTwo[0].strip()+ '\n'

            if setOne not in uniqueSet and setTwo not in uniqueSet:
                uniqueSet.append(setOne)

        self.__setOfValues = uniqueSet

    def __printFoundSets(self):

        if len(self.__setOfValues) > 0:
            for element in self.__setOfValues:
                print(element)
        else:
            print('Not Found')

obj = Problem2()