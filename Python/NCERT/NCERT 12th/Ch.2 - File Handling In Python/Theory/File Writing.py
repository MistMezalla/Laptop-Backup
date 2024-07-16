with open('my file.txt','w') as fr1:
    list1=['Hello Everyone\n','My name is Harshal\n',"Let's GO\n"]

    print(fr1.write(str(list1)))
    print(fr1.writelines(list1))

    list2=('1,2,3,4,5,6,7')

    print(fr1.writelines(list2))
    
