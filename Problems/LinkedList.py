class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.nodeCount = 0

    def addNode(self, newNodeVal):
        node = Node(newNodeVal)
        if self.head == None:
            self.head = node
        else:
            currentNode = self.head

            while(currentNode.nextval != None):
                currentNode = currentNode.nextval
            currentNode.nextval = node

        self.nodeCount += 1

    def addAtBegining(self, newNodeVal):
        node = Node(newNodeVal)
        if self.head == None:
            self.head = node
        else:
            node.nextval = self.head
            self.head = node

        self.nodeCount += 1

    def addAtPosition(self, newNodeVal, position):
        if(position >= self.nodeCount):
            self.addNode(newNodeVal)
        else:
            currentCount = 1
            currentNode = self.head
            while currentCount < position:
                currentCount += 1
                currentNode = currentNode.nextval

            refNode = currentNode.nextval
            node = Node(newNodeVal)
            node.nextval = refNode
            currentNode.nextval = node
            self.nodeCount += 1

    def removeNode(self, nodeVal):
        if self.nodeCount == 0:
            print("Linked List empty")
        else:
            currentNode = self.head
            prevNode = None
            found = False
            count = self.nodeCount
            while (count):
                if(currentNode.dataval == nodeVal):
                    found = True
                    break
                else:
                    prevNode = currentNode
                    currentNode = currentNode.nextval
                count -= 1

            if found == True:
                refNode = currentNode.nextval
                prevNode.nextval = refNode
                del currentNode
                self.nodeCount -= 1
            else:
                print("Not found")


    def traverList(self):
        currentNode = self.head
        count = self.nodeCount
        while (count):
            print(currentNode.dataval)
            currentNode = currentNode.nextval
            count -= 1
        print("#########")

linkedList = LinkedList()
linkedList.addNode("Surveer")
linkedList.addNode("Amit")
#linkedList.traverList()
linkedList.addAtBegining("Bala")
#linkedList.traverList()
linkedList.addAtPosition("Shashank", 1)
#linkedList.traverList()
linkedList.removeNode("Amit")
linkedList.traverList()