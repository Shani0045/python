#Stack Implementation Via Linked list

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
class Stack:
    def __init__(self):
        self.size = 0
        self.head = None
        
    def printS(self):
        curr = self.head
        if not curr:
            print("Stack is empty")
        while curr:
            print(curr.data)
            curr = curr.next
            
    def push(self,data):
        node = Node(data)
        node.next = self.head
        self.head = node
        self.size+=1
            
    def pop(self):
        if self.head is not None:
            deleted_node = self.head
            self.head = self.head.next
            self.size-=1
            return deleted_node.data
        
        else:
            print("Stack is already empty")
            
    def emptyStack(self):
        self.head = None
        self.size = 0
        
    def getSize(self):
        return self.size
        
