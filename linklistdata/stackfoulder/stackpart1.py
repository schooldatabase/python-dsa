""" ---------------------------- STACK USE IN PYTHON -------------------------------"""
class Stack(object):
    def __init__(self,limit=3):
        self.stack = []
        self.limit = limit
        print("\n_________________ STACK COMPILE _________________\n")
        
    def print_stack(self):
        if len(self.stack) <= 0:
            print('stack list empty and stack lenght less then equal zeros ')
        else:
            print('stack list current item  = ',self.stack)
            
    def push(self, data):
        """ python build in list function 'append' we can use list of add item in list/stack """
        if len(self.stack) >= self.limit:
            print('Stack is Full')
        else:
            self.stack.append(data)   
            print("stack data append -> ",data," stack list append - ",self.stack)
    
    def pop(self):
        """ python build in list function 'pop'  we can use list remove item in list/stack """
        if len(self.stack) <= 0:
            return None
        else:
            element = self.stack.pop()
            print("------------ remove stack item ----",element)
            
    def isEmpty(self):
        if len(self.stack) <= 0:
            print('STACK IS EMPTY')
        else:
            print('STACK IS NOT EMPTY')
            
if __name__ == '__main__':
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.pop()
    stack.pop()
    stack.pop()
    stack.isEmpty()
    stack.push(3)
    stack.push(4)
    stack.push(5)
    stack.push(6)
    stack.print_stack()
    
    
    

"""_________________ STACK COMPILE _________________

stack data append ->  1  stack list append -  [1]
stack data append ->  2  stack list append -  [1, 2]
------------ remove stack item ---- 2
------------ remove stack item ---- 1
STACK IS EMPTY
stack data append ->  3  stack list append -  [3]
stack data append ->  4  stack list append -  [3, 4]
stack data append ->  5  stack list append -  [3, 4, 5]
Stack is Full
stack list current item  =  [3, 4, 5]"""