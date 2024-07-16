def search():
    list1=[]
    n=int(input('enter the number of element to be entered: '))
    for i in range(1,n+1):
        elements=float(input('enter the number: '))
        list1.append(elements)
    print(list1)

    num=float(input('enter the number to be found: '))
    if num in list1:
        pos=list1.index(num)
        print('the number is ',num,'\nand its postion is',pos)

    else:
        print('the given number not in list')


search()
