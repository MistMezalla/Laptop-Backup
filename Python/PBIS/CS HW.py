#Program to check even or not

num1=int(input("Enter the number to be checked: "))
rem=num1%2

if rem==0:
    print("Even number")

else:
    print("Odd number")

#Sum of Nat nos

n=int(input("Enter the natural number upto which sum is to be calculated: "))
sum=0

for N in range(1,n+1):
      sum=sum+N

print("Sum= ",sum)

#Program for choice in area

c=int(input("Below are codes for finding the areas of respective polgons:\n 1=area of circle\n 2=area of parallelogram\n 3=area of square\n Enter the code: "))

if c==1:
      r=int(input("Enter the radius of circle: "))
      a=3.14*(r**2)
      print("area= ",a)

elif c==2:
      b=int(input("Enter the base of parallelogram: "))
      h=int(input("Enter the height of parallelogram: "))
      a=b*h
      print("area= ",a)

elif c==3:
    s=int(input("Enter the side of the square: "))
    a=s*s
    print("area= ",a)

else:
    print("wrong input")

#Leap Year
    
year=int(input("Enter the year to be checked: "))

rem=year%4

if rem==0:
    print("Leap Year")

else:
    print("Ordinary Year")

#To check the case of a string
    
str1=input("Enter the string whose case is to be checked: ")

if  str1.islower()==True:
    print("Lowercase")

elif str1.isupper()==True:
    print("Uppercase")

else :
    print("None")
    
    

            

      
