class Node:
    def __init__(self, value=0):
        self.value = value
        self.prev = None
        self.next = None


class doublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, value):
        newNode = Node(value)
        if self.length == 0:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            newNode.prev = self.tail
            self.tail = newNode
        self.length += 1
        return True

    def removeLast(self):  # Remove From Last
        if self.length == 0:
            return None
        if self.length == 1:
            temp = self.head
            self.head = self.tail = None
            self.length -= 1
            return temp
        temp = self.tail
        self.tail = self.tail.prev
        self.tail.next = None
        temp.prev = None
        self.length -= 1
        if self.length == 0:
            self.head = self.tail = None
        return temp

    def prepend(self, value):
        newNode = Node(value)
        if self.length == 0:
            self.head = newNode
            self.tail = newNode
            self.length += 1
            return True
        newNode.next = self.head
        self.head.prev = newNode
        self.head = newNode
        self.length += 1

    def removeFirst(self):
        if self.length == 0:
            return None
        if self.length == 1:
            self.head = self.tail = None
            self.length = 0
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.head.prev = None
        return temp

    def get(self, index):
        if index < 0 or index > self.length:
            return None
        if index < self.length // 2:
            temp = self.head
            for i in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for i in range(self.length - 1, index, -1):
                temp = temp.prev
        return temp

    def set(self, index, value):
        node = self.get(index)
        if not node:
            return False
        node.value = value
        return True

    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        elif index == self.length:
            return self.append(value)
        after = self.get(index)
        before = after.prev
        newNode = Node(value)
        before.next = newNode
        newNode.prev = before
        after.prev = newNode
        newNode.next = after
        self.length += 1
        return True

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.removeFirst()
        if index == self.length - 1:
            return self.removeLast()
        removeNode = self.get(index)
        before = removeNode.prev
        before.next = removeNode.next
        removeNode.prev, removeNode.next = None, None
        return removeNode

    def __str__(self):
        linearDisplay = ""
        temp = self.head
        while temp != None:
            linearDisplay += str(temp.value)
            linearDisplay+= "-->" if temp.next != None else ""
            temp = temp.next
        return (str(linearDisplay))

    def reverse(self):
        if self.head==None:
            return None
        if self.head==self.tail:
            return True
        tempHead=self.head
        tempTail=self.tail
        for i in range(self.length//2):
            tempTail.value,tempHead.value=tempHead.value,tempTail.value
            tempTail=tempTail.prev
            tempHead=tempHead.next
            print(tempHead.value,tempTail.value)
        return True

    def search(self,value):
        temp=self.head
        length=0
        while length<self.length and temp.value!=value:
            length+=1
            temp=temp.next
        if temp==None or temp.value!=value:
            return None
        return length

    def delete(self):
        prev=temp=self.head
        self.length=0
        while temp!=None:
            prev.next=None
            prev.value=None
            prev=temp
            temp=temp.next
        self.head=None



dlinkedList = doublyLinkedList()
if __name__ == '__main__':
    while 1:
        n = int(input("Enter 1.Display Linked List.\n2.Insert at First.\n3.Insert at End."
"\n4.Insert at Position.\n5.Remove at First.\n6.Remove at last.\n7.Remove at Position."
"\n8.Get value at position\n9.Set or Update value at position"
"\n10Reverse LinkedList.\n11.Delete all node.\n12.Search.\n13.Exit...."))
        if n == 1:
            print(str(dlinkedList).center(175," "))
        if n == 2:
            dlinkedList.prepend(int(input()))
        if n == 3:
            dlinkedList.append(int(input()))
        if n == 4:
            dlinkedList.insert(*map(int, input().split()))
        if n == 5:
            dlinkedList.removeFirst()
        if n == 6:
            dlinkedList.removeLast()
        if n == 7:
            dlinkedList.remove(int(input()))
        if n == 8:
            val=dlinkedList.get(int(input())).value
            print(str(val).center(175,' '))
        if n == 9:
            dlinkedList.set(*map(int, input("Enter Index and Value").split()))
        if n==10:
            dlinkedList.reverse()
            print(dlinkedList)
        if n==11:
            dlinkedList.delete()
        if n == 12:
            print(dlinkedList.search(int(input())))
        if n == 13:
            print("\n","Ending".center(175, "."))
            break
