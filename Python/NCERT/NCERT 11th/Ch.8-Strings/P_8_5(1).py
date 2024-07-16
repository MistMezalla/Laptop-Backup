def palindrome(string):
    j=0
    for i in range(-1,-len(string)-1,-1):
        if string[j]!=string[i]:
            print('not palindrome')
            break
        j+=1
    else:
        print('palindrome')

str1=input('enter the string: ')
palindrome(str1)

#Imp Note(see notebook for flow of execution description of the abv program).
'''most of the errors made by me can be overcomed if the flow of execution of
program is correctly mapped in my mind. Wrong or ambigous or no mapping has lead
to an error in majority of cases.'''

