import copy
l1=[1,2,[3,4,20],[5,6,[7,8,9]],10]
l2=l1.copy() #Creates shallow copy : O(n)
'''
Shallow copy:-
Creates a new object but does not create copies of nested objects. Instead, it copies the references to those objects.
'''
l3=copy.deepcopy(l1) #Creates Deep Copy : O(n)
'''
Deep Copy:-
Creates a new object and recursively copies all objects found in the original, meaning it duplicates the nested objects 
as well.
'''
l4=l1 #serves as ref to l1 : O(1)

print("First lvl")
# First Level of Copy(surface lvl)
l2[0]=25
l3[1]=50
l4[4]=100
print(l1,l2,l3,l4,sep="\n")
print("sec level")

# Second Level of copy(deeper level)
l2[2][0]=-25
l3[2][1]=-50
l4[2][2]=-100
print(l1,l2,l3,l4,sep="\n")

print("3rd lvl")
# 3rd lvl of copy(more deep lvl)
l2[3][2][0]=99
l3[3][2][1]=999
l4[3][2][2]=9999
print(l1,l2,l3,l4,sep="\n")

