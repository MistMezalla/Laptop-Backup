import pickle
student=[]
f=open('Student.dat','wb')
ans='y'
while ans.lower()=='y':
    roll = int(input('Enter the Roll Number: '))
    name = input('Enter Name: ')
    marks= int(input('Enter the marks: '))
    student.append([roll,name,marks])
    ans=input('Add More? If yes enter (Y), if no enter(N)')
    if ans.lower() == 'n':
        break
pickle.dump(student,f)
f.close()

f=open('Student.dat','rb+')
student=[]
while True:
    try:
        student=pickle.load(f)
    except EOFError:
        break
ans='y'
while ans.lower()=='y':
    found=False
    r = int(input('Enter the Roll Number to update: '))
    for s in student:
        if s[0]==r:
            print('##Name is: ',s[1],' ##')
            print('##Current marks is: ',s[2],' ##')
            m = int(input('Enter the ne marks: '))
            s[2]=m
            print('## Record is updated ##')
            found=True
            break
        if not found:
            print('####Sorry! Roll number not found####')
    ans=input('Update more? If yes enter (Y), if no enter(N)')
    if ans.lower() == 'n':
        break
f.close()












            
