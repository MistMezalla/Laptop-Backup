mylist=[10,20,30,40,50,60,70,80,90]

choice=0

while True:
    print(mylist)
    print('1. Append an element\n2.Display the list\n3.Exit')
    choice=int(input('enter your choice from 1 to 3: '))

    if choice == 1:
        element=input('enter the element to be appended: ')
        mylist.append(element)

    elif choice == 2:
        print(mylist)

    elif choice ==3:
        break

    else:
        print('wrong input for choice')
        print('\n\nPress any key to continue.........')
        ch=input()

'''
Since the condition is in the while loop is 'True' which is not a variable,
hence the condition for while loop will always remain true and the loop will
iterate infinetly. FOr coming out of loop only wayy is the 'break' statement.
If we wanted to come out of the loop without 'break' then we had to assign a
variable in the condition section of while loop as say 'flag', where flag
before while loop is 'flag=True'. Then by making flag as false inside while
loop we can come out of the while loop.
'''
