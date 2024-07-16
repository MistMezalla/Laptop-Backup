with open('Trial1.txt','w+') as fw:
    lines=('1,2,3,4,5')
    fw.writelines(lines)
    fw.flush()
    t=fw.read()
    print(t)


myfile = open(r"C:/Users/Harshal Sanas/Desktop/Python/Myfile.txt")
line_count = 0
data = myfile.readlines()
for line in data:
    if line[0] == 'T':
        line_count += 1
print(line_count)
myfile.close()

def ChangeVal(M,N):
    for i in range(N):
        if M[i]%5 == 0:
            M[i]//=5
        if M[i]%3 == 0:
            M[i]//=3
L = [25,8,75,12]
ChangeVal(L,4)
for i in L:
    print(i,end="#")
print()

print(4.00/(2.0 + 2.0))

print(''' Eina
\nNina
\nDika''')

print('Eina\nNina\nDika')

print(float('-infinity'))
print(float('inf'))

print("HEllo World")

print("hello\\example\\test.txt")
