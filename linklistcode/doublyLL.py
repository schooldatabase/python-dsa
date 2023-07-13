""" ---------------------------- DOUBLE LINKLIST CODE USE IN PYTHON -------------------------------"""

class Node:
    def __init__(self,data):
        self.data = data
        self.nref = None
        self.pref = None
        
class doublyLL:
    def __init__(self):
        self.head = None
        
    def print_LL(self):
        if self.head is None:
            print("Linked list is Empty!")
        else:
            n = self.head
            while n is not None:
                print(n.data,"-->",end=" ")
                n = n.nref
            print("None")

    def print_LL_reverse(self):
        if self.head is None:
            print("Linked list is Empty")
        else:
            n = self.head
            while n.nref is not None:
                n = n.nref
            while n is not None:
                print(n.data,"-->",end=" ")
                n = n.pref
            print("None")
                
    def add_begin(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.nref = self.head
            self.head.pref = new_node
            self.head = new_node
            
    def add_end(self,data):
        new_node = Node(data)
        if self.head is Node:
            self.head = new_node
        else:
            n = self.head
            while n.nref is not None:
                n = n.nref
            n.nref = new_node
            new_node.pref = n
        
dll = doublyLL()
print("\n----------- doubly Linked list -----------")
print("\n---------- add begin  ----------\n")
dll.add_begin(10)
dll.add_begin(20)
dll.add_begin(30)
dll.print_LL()
print("\n---------- add end  ----------\n")
dll.add_end(40)
dll.add_end(50)
dll.add_end(50)
dll.print_LL()
print("\n---------- print list  ----------\n")
dll.print_LL()
print("\n---------- print reverse  ----------\n")
dll.print_LL_reverse()








"""
----------------------output ------------------------
----------- doubly Linked list -----------

---------- add begin  ----------

30 --> 20 --> 10 --> None

---------- add end  ----------

30 --> 20 --> 10 --> 40 --> 50 --> 50 --> None

---------- print list  ----------

30 --> 20 --> 10 --> 40 --> 50 --> 50 --> None

---------- print reverse  ----------

50 --> 50 --> 40 --> 10 --> 20 --> 30 --> None"""