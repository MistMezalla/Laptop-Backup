def avg_marks(n):
    list1=[]
    for i in range(1,n+1):
        print('enter the marks of student',i,': ',end='')
        marks=float(input())
        list1.append(marks) 
    total=sum(list1)
    avg=total/n
    print('Average is', avg)

number_of_students=int(input('enter the number of students whose avg is to be found: '))
avg_marks(number_of_students)


#marks=float(input('enter the marks of student',(i),': '))
'''
in the abv comment we can see that 'i' is an argument for input function.
however the input function takes atmost 1 argument. thus when n>1 then error is
diplayed.
'''
