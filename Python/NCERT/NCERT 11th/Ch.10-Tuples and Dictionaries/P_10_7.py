str1=input('enter the string to be checked: ')

dict1={}
for char in str1:
    if char in dict1:
        dict1[char]+=1
    else:
        dict1[char]=1

print(dict1)
    
