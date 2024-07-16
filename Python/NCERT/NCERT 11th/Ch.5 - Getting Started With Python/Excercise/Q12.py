#Q12
x=int(input('Enter the days to complete the work alone by A: '))
y=int(input('Enter the days to complete the work alone by B: '))
z=int(input('Enter the days to complete the work alone by C: '))

Total_Days=x*y*z/(x*y+y*z+x*z)

print('Total days is ',Total_Days)
