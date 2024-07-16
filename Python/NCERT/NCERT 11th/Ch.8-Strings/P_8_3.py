def word_reversal(string):
    
    for i in range(-1,-(len(string))-1,-1):
        print(string[i],end='')


str1=input('enter the string: ')
word_reversal(str1)

# errors committed
'''in range the step value by default is 1. Hence when no step value was mentioned the output was blank.'''
