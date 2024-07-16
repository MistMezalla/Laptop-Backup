'''def vowel_replace(string):
    vow= ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    for vow in string:
        print(string.replace(vow,'*'))
        
    else:
        print(string)

str1=input('enter the string: ')

vowel_replace(str1)'''

'''str1='Hellom Everyone'
vow=['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
print(str1.replace(vow,'*')) #the arguments in replace must be string and not list or any other data type.
'''
def vowel_replace(string):
    newstr=''
    for char in string:
        if char in 'aeiouAEIOU':
            newstr+='*'
        else:
            newstr+=char

    print(newstr)

str1=input('enter the string: ')
vowel_replace(str1)
