#Program 5-1:-
print("Hello world")

#Program 5-3:-
length=10
breadth=20
area=length*breadth
print(area)

#Program 5-4:-
num1=23
num2=34
product=num1*num2
print(product)

#Use of ID
print(id(num1))
id(num2)
id(product)
t=id(num2)
print(t)

#Syntax for the use of id function is correctly displayed by num1 and not by num2 and product
num1=89
print(id(num1))
 
#Example 5.3
num3=57
print(type(num1))
var1=True
print(type(var1))
num4=5.67
print(type(num4))
num5=-7+8j
print(type(num5))

#string, tuple and list
str1='hi' 
print(str1)

list1=[10,4,789,'hello']
print(list1)
list1.append(234)
print(list1)
#Thus a list is mutuable whereas tuple is immutable.

tuple1=(9,876,'go',98)
print(tuple1)
#098 is invalid as leading zeroes are not accepted. Hence it should be 98.

#set
set1={54,908,'towads',77}
print(set1)

#Dictionary
dict1={'wheat':34,'rice':50}
print(dict1)
print(dict1['rice'])

#only corresponding value of key is valid for print(dict1[key]) wil give value corresponding to key in[]; whereas key for value is invalid,i.e, print(dic1[value]) will give error

list2=[]
print(type(list2))

