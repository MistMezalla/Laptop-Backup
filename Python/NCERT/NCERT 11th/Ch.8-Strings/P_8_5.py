def palindrome(string):
    for i in range(-1,-len(string)-1,-1):
        
        string_r=string[i]
        print(string_r,end='')

str1=input('enter the string: ')
palindrome(str1)

'''if str(str1)==str(t):
    print('entered string is palindrome')

else:
     print('not palindrome')'''

        
    
