try:
    num=100
    den=int(input())
    ans=num/den

except ZeroDivisionError:
    print('Enter a non zero value')

else:
    print(ans)

finally:
    print(1020)
    print('bye')
    for i in range(0,5):
        print('Welcome')
