class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
class MyLinkedList(object):

    def __init__(self):
        self.head = None

    def get(self, index):
        temp = self.head
        i=0
        while temp is not None:
            if i == index:
                return temp.val
            temp = temp.next
            i += 1 
        return -1

    def addAtHead(self, val):
        nn = Node(val)
        nn.next = self.head
        self.head = nn
        

    def addAtTail(self, val):
        nn = Node(val)
        if self.head is None:
            self.head = nn
            return
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = nn

    def addAtIndex(self, index, val):
        
        if index < 0:
            return 
        if index == 0:
            self.addAtHead(val)
            return
        temp = self.head
        i=0
        while i < index-1:
            if temp is None:
                return
            temp = temp.next
            i += 1
        if temp is None:
            return
        nn = Node(val)
        nn.next = temp.next
        temp.next = nn
    

        

    def deleteAtIndex(self, index):
        if index < 0 or self.head is None:
            return
        if index == 0:
            self.head = self.head.next
            return
        temp = self.head
        i=0
        while i < index-1:
            if temp is None:
                return
            temp = temp.next
            i += 1
        if temp is None or temp.next is None:
            return
        temp.next = temp.next.next

        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)