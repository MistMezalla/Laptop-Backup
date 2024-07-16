'''
                            Fibonacci Sequence Module
This module will help to find the fibonacci sequence upto the entered terms.
'''

def Fibonacci_sequence(t):
    term1=0
    term2=1

    if t<1:
        print('wrong input \nenter a natural number')
    elif t==1:
        print(term1)

    elif t==2:
        list1=[term1,term2]
        print(list1)
    else:
        FS=[term1,term2]
        for i in range(1,t-1):
            n=len(FS)
            term=FS[n-1] + FS[n-2]
            FS.append(term)
            
        
        print('Fibonacci sequence for 1st', t, 'terms is',FS)

terms=int(input('enter the terms upto which fibonacci sequence is to found: '))
Fibonacci_sequence(terms)

# for docstring to come first hide the last two statement for docstring.

        
    
    
