
class Node:
 
    # Constructor to initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None
 
class LinkedList:
    def __init__(self):
        self.head=None
    
    def push(self,data):
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node
        
    def printList(self):
        temp = self.head
        while(temp):
            print temp.data,
            temp = temp.next
    
    def reverselist(self):
        current=self.head
        prev = None
        while(current is not None):
            next=current.next
            current.next=prev
            prev=current
            current=next
        self.head=prev
    

 
 
# Driver program to test above functions
llist = LinkedList()
llist.push(20)
llist.push(4)
llist.push(15)
llist.push(85)    
llist.printList()
llist.reverselist()
llist.printList()
