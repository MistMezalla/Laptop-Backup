#program to display the Fibonacci Sequence upto n-th term

nterms = int(input('How may terms? '))

#frist two terms
n1,n2=0,1
count=0

#check if the number of terms is valid
if nterms <= 0:
    print('Please enter a positive integer')
elif nterms == 1:
    print('Fibonacci sequence upto',nterms,':')
    print(n1)
else:
    print('Fiboncci Sequence: ')
    while count < nterms:
        print(n1)
        nth = n1+n2
        #update values
        n1=n2
        n2=nth
        count+=1
