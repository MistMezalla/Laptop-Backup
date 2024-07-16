queue=list()
shuttlecocks=[]

number=int(input('enter the number of shuttlecocks to be inserted: '))
for i in range(0,number):
    item=input('enter the id for shuttlecock to be inserted: ')
    shuttlecocks.append(item)
print(shuttlecocks)

def ENQUEUE(queue,shuttlecocks):
    for item in shuttlecocks:
        queue.append(item)
    print(queue)

def isEMPTY(queue):
    n=len(queue)
    if n==0:
        return True
    else:
        return False

def DISPLAY(queue):
    n=len(queue)
    print('items in the queue are: ')
    for i in range(0,n):
        print(queue[i])

def DEQUEUE(queue):
    if not (isEMPTY(queue)):
        queue.pop(0)
    else:
        print('Underflow')

def PEEK(queue):
    print(queue[0])
    
ENQUEUE(queue,shuttlecocks)
DISPLAY(queue)
DEQUEUE(queue)
PEEK(queue)
