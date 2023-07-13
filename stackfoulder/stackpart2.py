""" ---------------------------- STACK USE IN PYTHON -------------------------------"""
stack=[]

n = int(input("limit of stack:"))
def push():
    if len(stack)==n:
        print("list is Full!")
    else:
            
        element = input("Enter the element -> ")
        stack.append(element)
        print("append element ",stack)
    
def pop_element():
    if not stack:
        print("stack is empty !")
    else:
        e = stack.pop()
        print("removed element:",e)
        print(stack)
while True:
    print("Select the opertion 1. push 2. pop 3. quit")
    choice = int(input())
    if choice==1:
        push()
    elif choice==2:
        pop_element()
    elif choice==3:
        break
    else:
        print("Enter the correct operation !")