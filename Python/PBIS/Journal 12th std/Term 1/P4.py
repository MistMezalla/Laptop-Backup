import pickle
student=[]
f=open('student.dat','wb')
ans='y'
while ans.lower()=='y':
    roll = int(input('Enter the Roll Number: '))
    name = input('Enter Name: ')
    student.append([roll,name])
    ans=input('Add More? If yes enter (Y), if no enter(N)')
    if ans.lower() == 'n':
        break
pickle.dump(student,f)
f.close()

f=open('student.dat','rb')
student=[]
while True:
    try:
        student=pickle.load(f)
    except EOFError:
        break
ans='y'
while ans.lower()=='y':
    found=False
    r = int(input('Enter the Roll Number to search: '))
    for s in student:
        if s[0]==r:
            print('##Name is: ',s[1],' ##')
            found=True
            break
        if not found:
            print('####Sorry! Roll number not found####')
    ans=input('Search more? If yes enter (Y), if no enter(N)')
    if ans.lower()== 'n':
        break
f.close()
