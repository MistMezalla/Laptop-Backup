import csv 
fh=open("student.csv","r") 
stureader=csv.reader(fh) 
for rec in stureader: 
    print(rec) 
fh.close()
