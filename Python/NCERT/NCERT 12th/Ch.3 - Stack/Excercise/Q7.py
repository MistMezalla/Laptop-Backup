stack=list()
num_list=[]
even=[]

numbers=int(input('how many numbers u wnat to enter?: '))
for i in range(0,numbers):
    num=int(input('Enter the numbers: '))
    num_list.append(num)

def PUSH(stack,num_list):
    for item in num_list:
        if item%2==1:
            stack.append(item)  
        else:
            even.append(item)
                  
def DISPLAY(stack):
    n=len(stack)
    print('data in the stack is:')
    for i in range(n-1,-1,-1):
        print(stack[i])

def LARGEST_1(stack):
    ind=stack.index(max(stack))
    n=len(stack)
    for i in range(n-1,ind-1,-1):
        largest=stack.pop()
    print('largest number in the stack is',largest) 

def LARGEST_2(stack):
    popped=[]
    n=len(stack)
    for i in range(0,n):
        num=stack.pop()
        popped.append(num)
        #print(popped)
        if num==max(popped):
            largest=num
    #print(largest)
    print('largest number in the stack is',largest) 
        
    
PUSH(stack,num_list)
DISPLAY(stack)
LARGEST_1(stack)
#LARGEST_2(stack)    
        

