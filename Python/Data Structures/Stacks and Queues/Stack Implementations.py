from collections import deque
from queue import LifoQueue

def collections_deque():
    stack = deque()

    ch = int(input("1=push\n2=pop\n3=size\n4=print\n5=TOS\n0=exit\nEnter: "))

    while(ch):
        if (ch==1):
            stack.append((eval(input("Enter the val to be pushed: "))))
        elif ch==2:
            print("Value popped: ",stack.pop())
        elif ch==3:
            print("Size=",len(stack))
        elif ch==4:
            print(stack)
        elif ch==5:
            print("TOS=",stack[-1])

        ch = int(input("1=push\n2=pop\n3=size\n4=print\n0=exit\nEnter: "))

'''
Implement after learning multithreading concept in pyhton.
For class implementation make use of:-
-> help(LifoQueue) to view the description
-> Inherit 'LifoQueue' as parent class.
'''
def queue_LifoQueue():
    stack = LifoQueue(maxsize=int(input("Enter the size of the stack: ")))

    ch = int(input("1=push\n2=pop\n3=size\n4=print\n5=TOS\n0=exit\nEnter: "))

    while (ch):
        if (ch == 1):
            if (stack.full()):
                print("Stack is full. Pop elem to add new.")
            stack.put((eval(input("Enter the val to be pushed: "))))

        elif ch == 2:
            print("Value popped: ", stack.get())
        elif ch == 3:
            print("Size=", stack.qsize())
        elif ch == 4:
            print(stack)
        elif ch == 5:
            '''print("TOS=", stack[-1])'''

        ch = int(input("1=push\n2=pop\n3=size\n4=print\n0=exit\nEnter: "))

#collections_deque()
#queue_LifoQueue()

