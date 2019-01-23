from LinkedListDS.Node import Node


class LinkedList:
    def __init__(self):
        self.head = None
        self.counter = 0

    def getCount(self):
        print(self.counter)

    def insertAtStart(self, data):
        newNode = Node(data)
        if not self.head:
            self.head = newNode
        else:
            # Move current node to last
            newNode.nextNode = self.head
            # make new node the first element
            self.head = newNode

        self.counter += 1

    def insertAtEnd(self, data):
        if self.head is None:
            self.insertAtStart(data)
            return

        newNode = Node(data)
        actualNode = self.head
        while actualNode.nextNode is not None:
            actualNode = actualNode.nextNode

        actualNode.nextNode = newNode
        self.counter += 1

    def remove(self, data):
        if not self.head:
            return

        if data == self.head:
            self.head = self.head.nextNode
        else:
            self.head.remove(data, self)
        self.counter -= 1

    def traverseList(self):
        if self.head is None:
            print("List is empty")
        actualNode = self.head
        while actualNode.nextNode is not None:
            print(actualNode.data)
            actualNode = actualNode.nextNode
        # to print last element
        print(actualNode.data)