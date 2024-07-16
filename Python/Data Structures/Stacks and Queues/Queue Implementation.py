from collections import deque

ch=int(input("1=enqueue\n2=dequeue\n3=size\n4=print\n0=exit\nEnter: "))

queue = deque()

while ch:
    if (ch == 1):
        queue.appendleft((eval(input("Enter the val to be pushed: "))))
    elif ch == 2:
        print("Value popped: ", queue.pop())
    elif ch == 3:
        print("Size=", len(queue))
    elif ch == 4:
        print(list(queue)[::-1])

    ch = int(input("1=push\n2=pop\n3=size\n4=print\n0=exit\nEnter: "))

