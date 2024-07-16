#Arguments to print function
#Appendix B (Sumita Arora)
x=10
y=20
def valid_print_arguments():
    print(x+y)

    print(print())

    print(print('hi'))

    print(input('Enter any data: '))

    t=print(11)
    print(type(t))
    print(type(11))

def invalid_print_arguments():
    "print(x=+5)"

    "print(z=x+y)"
    
    "print(a,b,c=1,2,3)"
    
#valid_print_arguments()

a,b=10,20
m,n=30.0,40.0
print(int(input("Enter any number: ")))
print()
#print(m,n,print(a,b),sep='\t')
print(m,input("Enter any char: "),print(a,b,int(input("Enter any number: "))),n,sep='\t')


