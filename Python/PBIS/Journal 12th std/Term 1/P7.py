import csv
a1=['id','password']
a=[['userid1','password1'],
   ['userid2','password2'],
   ['userid3','password3'],
   ['userid4','password4'],
   ['userid5','password5']]
b=input('Enter username')
myfile=open(r'sample.csv','w+',newline='\r\n')
myfile1=csv.writer(myfile)
myfile1.writerow(a1)
myfile1.writerows(a)
myfile.seek(0)
myfile2=csv.reader(myfile)
for i in myfile2:
    if i[0]==b:
        print('The password is ',i[1])
myfile.close()
   
