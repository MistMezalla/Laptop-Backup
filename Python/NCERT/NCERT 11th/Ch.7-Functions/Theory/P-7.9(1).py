def mixedFraction(num,den=1):
    if num%den!=0:
        q=int(num/den)
        r=num%den
        print(q,"(",r,'/',den,")")

    else:
        print('whole number')

num=int(input('Enter the numerator: '))
den=int(input('Enter the denominator: '))

if num>den:
    mixedFraction(num,den)

else:
    print('proper fraction')
