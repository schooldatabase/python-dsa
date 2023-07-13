""" ---------------------------- BINARY SEARCH TREE CODE USE IN PYTHON -------------------------------"""
class BST:
    def __init__(self,key):
        self.key = key
        self.lchild = None
        self.rchild = None
        
    def insert(self,data):
        if self.key is None:
            self.key = data
        if self.key == data:
            return
        if data < self.key:
            if self.lchild:
                self.lchild.insert(data)
            else:
                self.lchild = BST(data)
        else:
            if self.rchild:
                self.rchild.insert(data)
            else:
                self.rchild = BST(data)
                
    def search(self,data):
        if self.key == data:
            print("Node is Found")
        if data < self.key:
            if self.lchild:
                self.lchild.search(data)
            else:
                print("Node is not present in tree")
        else:
            if self.rchild:
                self.rchild.search(data)
            else:
                print("Node is not present in tree")
                
    def preorder(self):
        print(self.key, end=" ")
        if self.lchild:
            self.lchild.preorder()
        if self.rchild:
            self.rchild.preorder()
    
    def inorder(self):
        if self.lchild:
            self.lchild.inorder()
        print(self.key, end=" ")
        if self.rchild:
            self.rchild.inorder()
    
    def postorder(self):
        if self.lchild:
            self.lchild.postorder()
        if self.rchild:
            self.rchild.postorder()
        print(self.key,end=" ")
    def delete(self,data):
        if self.key is None:
            print("Tree is empty!")
            return
        if data < self.key:
            if self.lchild:
                self.lchild = self.lchild.delete(data)
            else:
                print("Given Node is Not present in the tree")
        elif data > self.key:
            if self.rchild:
                self.rchild = self.rchild.delete(data)
            else:
                print("Given Node is not present in the tree")
        else:
            if self.lchild is None:
                temp = self.rchild
                self = None
                return temp
            if self.rchild is None:
                temp = self.lchild
                self = None
                return temp
            
            node = self.rchild
            while node.lchild:
                node = node.lchild
            self.key - node.key
            self.rchild = self.rchild.delete(node.key)
        return self    
    # def delete(self,data,curr):
    #     if self.key is None:
    #         print("Tree is empty!")
    #         return
    #     if data < self.key:
    #         if self.lchild:
    #             self.lchild = self.lchild.delete(data,curr)
    #         else:
    #             print("Given Node is Not present in the tree")
    #     elif data > self.key:
    #         if self.rchild:
    #             self.rchild = self.rchild.delete(data,curr)
    #         else:
    #             print("Given Node is not present in the tree")
    #     else:
    #         if self.lchild is None:
    #             temp = self.rchild
    #             if data == curr:
    #                 self.key = temp.key
    #                 self.lchild = temp.lchild
    #                 self.rchild = temp.rchild
    #                 temp = None
    #                 return
    #             self = None
    #             return temp
    #         if self.rchild is None:
    #             temp = self.lchild
    #             if data == curr:
    #                 self.key = temp.key
    #                 self.lchild = temp.lchild
    #                 self.rchild = temp.rchild
    #                 temp = None
    #                 return
    #             self = None
    #             return temp
            
    #         node = self.rchild
    #         while node.lchild:
    #             node = node.lchild
    #         self.key - node.key
    #         self.rchild = self.rchild.delete(node.key)
    #     return self    
    
    # def count(node):
    #     if node is None:
    #         return 0
    #     return 1+count(node.lchild)+count(node.rchild)
    
    def min_node(self):
        print("-------------------")
        print(self.key)
        print(self.lchild)
        print(self.lchild.key)
        a = self.lchild.lchild
        b = self.lchild.rchild
        print(a.key,"  tttt  ",b.key)
        print("-------------------")
        current = self
        while current.lchild:
            print("BST Left Searching ..... ",current.key)
            current = current.lchild
            print("Searching ..... ",current.key)
        print("node with smallest key is : ", current.key)
        print("node with smallest key is : ", self.lchild.lchild.key)
        
    def max_node(self):
        current = self
        while current.rchild:
            print("dd",current.key - 1)
            current = current.rchild
        print("node with maximum key is :", current.key - 2)
    
root = BST(10)
list1 = [6,3,1,6,97,967,98,99,3,7]
for i in list1:
    root.insert(i)
print("Preorder")
root.preorder()
print()
print("Inorder")
root.inorder()
print()
print("postorder")
root.postorder()
print()
# root.delete(3)
# print("after deleting")
# root.preorder()

root.min_node()
root.max_node()






"""
 -----------------------output----------------------
Preorder
10 6 3 1 7 97 967 98 99 
Inorder
1 3 6 7 10 97 98 99 967
postorder
1 3 7 6 99 98 967 97 10
-------------------
10
<__main__.BST object at 0x0000023B68FD51D0>
6
3   tttt   7
-------------------
BST Left Searching .....  10
Searching .....  6
BST Left Searching .....  6
Searching .....  3
BST Left Searching .....  3
Searching .....  1
node with smallest key is :  1
node with smallest key is :  3
dd 9
dd 96
node with maximum key is : 965

        """