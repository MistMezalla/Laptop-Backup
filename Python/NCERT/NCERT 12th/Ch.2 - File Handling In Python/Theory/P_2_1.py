with open(r'testfile.txt','w') as fw1:
    n=int(input('Enter th number of lines to be entered: '))
    for i in range (1,n+1):
        lines=input('enter the lines to be written: ')
        fw1.writelines(list(lines))

fr1=open(r'testfile.txt','r')
var1=fr1.read()
print(var1)
fr1.close()

    
