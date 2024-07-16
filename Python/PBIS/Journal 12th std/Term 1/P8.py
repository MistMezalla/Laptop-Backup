def isPalindrome(s):
    return s==s[::-1]

s=str(input('enter the string data '))
ans=isPalindrome(s)

if ans:
    print('Yes')
else:
    print('No')


