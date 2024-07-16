num1=int(input('Enter the numbrer whose pattern is to be created: '))

for i in range (1,num1+1):
    for j in range (1,i+1):
        print(j, end='')# end is a parameter of the print which is a built in function. If nothinf is specifeid in current line print command then print function would naturally print all the values of a single loop one below the other i.e default value of end is \n. Thus to print the values of given loop in one line we use end and can also specify the space between each value.
    print()

