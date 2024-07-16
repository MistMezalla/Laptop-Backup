def tuple_max_min(n):
    list=[]
    for i in range(0,n):
        num=input('enter the number to be addded: ')
        list.append(num)
        tuple1=tuple(list)
    print(max(tuple1),min(tuple1),sep='\n')

n=int(input('enter the number of numbers to be added: '))
tuple_max_min(n)
