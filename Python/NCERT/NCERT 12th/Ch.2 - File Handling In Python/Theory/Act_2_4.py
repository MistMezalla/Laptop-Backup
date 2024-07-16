with open(r'C:/Users/Harshal Sanas/Desktop/hello.txt','r') as fr1:
    print(fr1.tell())
    
    var1=fr1.readline()
    
    while var1:
        print(var1,end='')
        var1=fr1.readline()
    '''
    print(fr1.read())
    '''
    
    '''
    In pyhton epmty string list tuple or any data type is logically false. Hence
    check the output of the below code to verify the output of the abv code.
    

    print(list(fr1.readline()))
    print(list(fr1.readline()))
    print(list(fr1.readline()))
    print(list(fr1.readline()))
    print(list(fr1.readline()))
    print(list(fr1.readline()))

    '''
