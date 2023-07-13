""" ---------------------------- LINKLIST CODE USE IN PYTHON -------------------------------"""
class Node:
    def __init__(self,data):
        self.data = data
        self.ref = None
  

class LinkedList:
    def __init__(self):
        self.head = None
        
    def print_LL(self):
        if self.head is None:
            print("Linked list is empty!")
        else:
            n = self.head
            while n is not None:
                print(n.data,"-->",end=" ")
                n = n.ref
            print("None")
    
    def add_begin(self,data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node
            
    def add_end(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.ref is not None:
                n = n.ref
            n.ref = new_node
    
    def add_after(self,data,x):
        n = self.head
        while n is not None:
            if x==n.data:
                break
            n = n.ref
        if n is None:
            print("node is not present in LL")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node
        
    def add_before(self,data,x):
        if self.head is None:
            print("Linked List is empty!")
            return
        if self.head.data==x:
            new_node = Node(data)
            new_node.ref = self.head
            self.head = new_node
            return
        n = self.head
        while n.ref is not None:
            if n.ref.data==x:
                break
            n = n.ref
        if n.ref is None:
            print("Node is not found!")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node
    
    def delete_begin(self):
        if self.head is None:
            print("Linked list is empty so we can't delete nodes!")
        else:
            self.head = self.head.ref
    
    def delete_end(self):
        if self.head is None:
            print("Linked list is Empty !")
        elif self.head.ref is None:
            self.head = None
        else:
            n = self.head
            while n.ref.ref is not None:
                n = n.ref
            n.ref = None
    
    def delete_by_any_value(self,x):
        if self.head is None:
            print("can't delete Linked list is Empty !")
            return
        if x==self.head.data:
            self.head = self.head.ref
            return
        n = self.head
        while n.ref is not None:
            if x==n.ref.data:
                break
            n = n.ref
        if n.ref is None:
            print("Node is not present!")
        else:
            n.ref = n.ref.ref
                
        
    
    # def inset_empty(self,data):
    #     if self.head is None:
    #         new_node = Node(data)
    #         self.head = new_node
    #     else:
    #         print("Linked list is not empty!")  # output current time ' Linked list is not empty! ' else 'data'
            
        
ll1 = LinkedList()
print("\n---------------- Single Linked List is implement ----------------\n")
ll1.add_begin(10)
ll1.add_begin(20)
ll1.add_end(30)
ll1.add_end(40)
ll1.print_LL()

print("\n-----before----\n")
ll1.add_before(15,10)
ll1.add_before(25,20)
ll1.add_before(28,17)
ll1.print_LL()

print("\n-----after-----\n")
ll1.add_after(50,30)
ll1.add_after(60,40)
ll1.add_after(70,500)
ll1.print_LL()

print("\n-----delete begin -----\n")
ll1.delete_begin()
ll1.delete_begin()
ll1.print_LL()

print("\n-----delete end -----\n")
ll1.delete_end()
ll1.delete_end()
ll1.print_LL()

print("\n----- delete_by_any_value -----\n")
ll1.delete_by_any_value(50)
ll1.delete_by_any_value(550)
ll1.delete_by_any_value(10)

# ll1.inset_empty(5)
ll1.print_LL()
        
        
"""---------------- Single Linked List is implement ----------------

20 --> 10 --> 30 --> 40 --> None

-----before----

Node is not found!
25 --> 20 --> 15 --> 10 --> 30 --> 40 --> None

-----after-----

node is not present in LL
25 --> 20 --> 15 --> 10 --> 30 --> 50 --> 40 --> 60 --> None

-----delete begin -----

15 --> 10 --> 30 --> 50 --> 40 --> 60 --> None

-----delete end -----

15 --> 10 --> 30 --> 50 --> None

----- delete_by_any_value -----

Node is not present!
15 --> 30 --> None
"""