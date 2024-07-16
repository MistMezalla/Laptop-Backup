#Lecture Questions
def HW_1():
    "Exp=1/1! + 2**2/2! + 3**3/3! + .... + n**2/n!"
    n=int(input("Enter the number: "))
    val=0;sm=0
    
    for i in range (1,n+1):
        num=1;den=1
        for j in range (1,i+1):
            num=num*i
            den=den*j      
        sm+=num/den
    print(sm)

c=0
while c==0:
    HW_1()
    c=int(input("Do u want to continue: 0 or 1"))
