#Linkedlist implemention

class Node:
    def __init__(self,data):
        self.data = data
        self.next= None
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def insertAtStart(self,data):
        node = Node(data)
        node.next = self.head
        self.head = node
    
    def printList(self):
        curr = self.head
        while curr is not None:
            print(curr.data)
            curr = curr.next
            
    def insertAtEnd(self,data):
        node = Node(data)
        curr = self.head
        if curr is None:
            self.head = node
        else: 
            while curr.next is not None:
                curr = curr.next

            curr.next = node
        
    def insertAtMiddle(self, mid, data):
        curr = self.head
        node = Node(data)
        f = 0
        
        if curr is None:
            self.head = node
        else:
            while curr is not None:
                if curr.data == mid:
                    f=1
                    break
                curr = curr.next
                
            if f==1:  
                node.next = curr.next
                curr.next = node
            else:
                print("Mid point not found...")
        
    def deleteAtStart(self):
        self.head = self.head.next
        
    def deleteAtEnd(self):
        curr=self.head
        if curr is None:
            print("no element found")
        else:
            while curr.next.next is not None:
                curr = curr.next    
            curr.next = None
            
    def deleteValue(self,value):
        curr=self.head
        if curr is None:
            print("no element found")
        else:
            while curr.next.data != value:
                curr = curr.next
                
            curr.next = curr.next.next
            
    def deleteIndex(self,index):
        curr=self.head
        i=0
        if curr is None:
            print("no element found")
        else:
            while curr is not None:
                if i == index:
                    break
                else:
                    curr = curr.next
                    i+=1
                
            curr.next = curr.next.next
            
    def max_node(self):
        curr = self.head
        max_node = curr
        
        while curr is not None:
            if max_node.data < curr.data:
                max_node = curr
            curr = curr.next
                
        print("maxinmum node is : ",max_node.data)
        
    def length(self):
        curr = self.head
        count = 0
        while curr is not None:
            count+=1
            curr = curr.next
            
        print("Total length of linked list: ",count)
        
    def search(self, value):
        curr = self.head
        i = 0
        while curr is not None:
            if curr.data == value:
              return i
            i+=1
            curr = curr.next
            
    def searchindex(self, index):
        curr = self.head
        i = 0
        while curr is not None:
            if i == index:
              return curr.data
            i+=1
            curr = curr.next
            
    def reverse(self):
        prev = None
        curr = self.head
        
        while curr is not None:
            next_node=curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        self.head  = prev
            
