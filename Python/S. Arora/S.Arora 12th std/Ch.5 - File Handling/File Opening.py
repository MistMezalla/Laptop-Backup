'''fr=open(r"C:/Users/Harshal Sanas/Desktop/Python/S.Arora 12th std/Trial.txt",'r+')
text=fr.read()
text1=fr.write('My name is HArshal\n')
text2=fr.read()
fr.close()
print(text)
print(text2,end='\n\n\n')

fr1=open(r'C:/Users/Harshal Sanas/Desktop/Python/Trial1.py','r')
t=fr1.read()
fr1.close

print(t)
'''

'''
opens only python and text file
'''

fr2=open(r"C:\Users\HARSHAL\Desktop\Python\S.Arora 12th std\Ch.5 - File Handling\poem(my mother at sixty six).txt",'r')
t2=fr2.read(5)
fr2.close()
for L in t2:
    print(L.upper())
print(list(t2))
print(t2)

'''fr3=open(r'C:/Users/Harshal Sanas/Desktop/Python/S.Arora 12th std/Trial_1.txt','r')
t3=fr3.read()
fr3.close()
print(fr3)
'''
