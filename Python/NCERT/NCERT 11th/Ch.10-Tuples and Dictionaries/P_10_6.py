dict1={}

n=int(input('enter the number of employees to be stored: '))

for i in range(1,n+1):
    name=input('enter the name of the employee: ')
    salary=float(input('enter the salary of the employee: '))
    dict1[name]=salary

#Reference
print('EMPLOYEE NAME','SALARY',sep='\t')

for k in dict1:
    print(k,dict1[k],sep='\t\t')
    
