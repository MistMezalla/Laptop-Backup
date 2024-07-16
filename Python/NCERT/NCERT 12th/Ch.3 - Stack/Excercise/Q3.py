stack=list()
rev_string=''

string=input('enter the string to be reversed: ')

def PUSH(stack,string):
    for char in string:
        stack.append(char)

def POP(stack,string):
    for i in range(0,len(stack)):
        element=stack.pop()
        #print(element)
        global rev_string
        rev_string+=element
    print(rev_string)

PUSH(stack,string)
POP(stack,string)
