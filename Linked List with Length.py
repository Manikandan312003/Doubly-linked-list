class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.length=0

    def listprint(self):
        printval = self.head
        print("Linear Traverse", end="None" if printval == None else "\n")
        while printval != None:
            print(printval.dataval, end="-->" if printval.next else "")
            printval = printval.next

        print("", end="\n")

    def reversePrint(self):
        printvalue = self.head

        def printreverse(head):
            if head == None:
                print("Reverse Print")
                return 0
            a = printreverse(head.next)
            print('' if a == 0 else "-->", head.dataval, end="", sep="")

        printreverse(printvalue)
        print("")

    def insert(self, data):
        newNode = Node(data)
        self.length+=1
        if (self.head != None):
            current = self.head
            while (current.next):
                current = current.next
            current.next = newNode
        else:
            self.head = newNode

    def prepend(self,value):
        newnode=Node(value)
        if self.length==0:
            self.head=newnode
            self.length=1
        else:
            newnode.next=self.head
            self.head=newnode

    def removeFirst(self):
        if self.head:
            self.length-=1
            next = self.head.next
            self.head = next

    def deleteLast(self):
        prev = self.head
        self.length-=1
        current = prev.next
        while current.next != None:
            prev = current
            current = current.next
        prev.next = None
        return current.dataval

print("""1.Insert
2.Delete at First
3.Delete at Last
4.Print
5.Reverse Print
6.Exit
7.Length""")
list=LinkedList()
def getIntInput():
    return int(input())
while 1:
    inp=input()
    if inp =='1':
        n=input()
        list.insert(n)
    elif inp=='2':
        list.removeFirst()
    elif inp=='3':
        print("Removed",list.deleteLast())
    elif inp=='4':
        list.listprint()
    elif inp=='5':
        list.reversePrint()
    elif inp=='6':
        break
    else:
        print(list.length)