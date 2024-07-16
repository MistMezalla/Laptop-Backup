deque=list()
st=input('enter the string to be checked for palindrome: ')

def INSERT_REAR(deque,st):
    for elem in st:
        deque.insert(0,elem)
    
def INSERT_FRONT(deque,st):
    for elem in st:
        deque.append(elem)
    
def DISPLAY(deque):
    n=len(deque)
    for i in range(0,n):
        print(deque[i])

def DELETE_FRONT(deque):
    if len(deque)==0:
        print('underflow')
    else:
        return deque.pop(0)

def DELETE_REAR(deque):
    if len(deque)==0:
        print('underflow')
    else:
        return deque.pop()

def palchecker(deque,st):  
    INSERT_FRONT(deque,st)

    c=True
    while c and len(deque)>1:
        x=DELETE_FRONT(deque)
        y=DELETE_REAR(deque)

        if x.lower()==y.lower():
            c=True
        elif x.lower()!=y.lower():
            c=False

    return c

result=palchecker(deque,st)
print(st,'is a palindrome:',result)        
        
