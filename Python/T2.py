'''age=input()'''

'''def BA (age) :
    if age < 13 :
        print ('Child')
      elif 13 <= age < 20 :
          print ('Teen')
      else :
          print ('Adult')
'''
# some error
'''
def MA (age) :
        if age < 13 :
            print ('Child')
        elif 13 <= age < 20 :
            print ('Teen')
        else :
            print ('Adult')
'''
# some error
''' 
print(MA(age))
print(BA(age))
'''
'''
if age < 13 :
    print ('Child')
'''
# some error
'''
s=0
t='T'
while t=='T':
        name=input('name of product')
        price=int(input('price'))
        qty=int(input('qty'))
        s+=price*qty
        t=input('do u want to continue, T or F')

print(s)

tax=s*5/100
print(tax)
total=s+tax
print(total)
'''
'''
n_1=int(input('n_1=?'))
n_2=int(input('n_2=?'))

if n_1 > n_2 :
        m=n_1
elif n_1 < n_2 :
        m=n_2
else:
        print('LCM is',n_1)
t=1
while t==1:
        if m%n_1==0 & m%n_2==0:
                print('LCM is',m)
                t=1
        else:
                m+=1
                t=0
'''
#Flow of execution error
'''
n1=int(input())
n2=int(input())

q1=n1/n2
q2=n2/n1

print(q1,q2)

if q1==0:
    print(n2)
elif q2==0:
    print(n1)
else:
    print('n1=n2')
''' 
#If else block error 
