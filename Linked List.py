class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None


class LinkedList:
    def __init__(self):
        self.headval = None

    def listprint(self):
        printval = self.headval
        print("Linear Traverse", end="None" if printval == None else "\n")
        while printval != None:
            print(printval.dataval, end="-->" if printval.nextval else "")
            printval = printval.nextval

        print("", end="\n")

    def reversePrint(self):
        printvalue = self.headval

        def printreverse(head):
            if head == None:
                print("Reverse Print")
                return 0
            a = printreverse(head.nextval)
            print('' if a == 0 else "-->", head.dataval, end="", sep="")

        printreverse(printvalue)
        print("")

    def insert(self, data):
        newNode = Node(data)
        if (self.headval != None):
            current = self.headval
            while (current.nextval):
                current = current.nextval
            current.nextval = newNode
        else:
            self.headval = newNode

    def pop(self):
        if self.headval:
            next = self.headval.nextval
            self.headval = next

    def deleteLast(self):
        prev = self.headval
        current = prev.nextval
        while current.nextval != None:
            prev = current
            current = current.nextval
        prev.nextval = None

print("""1.Insert
2.Delete at First
3.Delete at Last
4.Print
5.Reverse Print
6.Exit""")
list=LinkedList()
def getIntInput():
    return int(input())
while 1:
    inp=input()
    if inp =='1':
        n=input()
        list.insert(n)
    elif inp=='2':
        list.pop()
    elif inp=='3':
        list.deleteLast()
    elif inp=='4':
        list.listprint()
    elif inp=='5':
        list.reversePrint()
    elif inp=='6':
        break