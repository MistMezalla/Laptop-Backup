with open(r'C:/Users/Harshal Sanas/Desktop/Python/S.Arora 12th std/Trial_1.txt','w+') as fw:
    fw1=fw.read()
    t='My name is Harshal Sanas'
    fw2=fw.write(t)
    fw3=fw.read()
fw.close()
print(fw1,fw2,fw3)
