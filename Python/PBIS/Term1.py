#Q24
'''
L=[10,20,30,40,50]
L=L+5
print(L)
'''
#Q26
T=(10,20,30)
T=T+(40,)
print(T)

#Q28
S='GOOD MORNING'
print(S.capitalize(),S.title(),end='!')
print()

#30
D={}
T=('a','b','c','d')
for i in range(1,5):
    D[i]=T[i-1]
print(D)

#Q35
from random import randrange
for N in range(2,5,2):
    print(randrange(1,N),end='#')
print()

#Q36
def FS(S):
    T=''
    for i in S:
        if i.isdigit():
            T=T+i
    return T

X='PYTHON 3.9'
Y=FS(X)
print(X,Y,sep='*')

#Q40
F=open('Rhymes.txt')
L=F.readlines()
for i in L:
    S=i.split()
    print(len(S),end='#')
print()

#Q42
F=open('Rhymes_1.txt')
S=F.read()
l=S.split()
print(L)
for i in L:
    if len(i)%3 != 0:
        print(i,end='')
print()
        

#Q46
F=open('Rhymes.txt')
L=F.readlines()
X=['the','ock']
for i in L:
    for W in i.split():
        if W in X:
            print(W,end='*')
    



