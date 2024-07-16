def mixedFraction(num,den=1):
    if num%den!=0:
        q=int(num/den)
        r=num%den
        print(q,"(",r,'/',den,")")

    else:
        print('whole number')

mixedFraction(9)
