stu_db = {89: {'Harshal': 9.0}, 101: {'Junaid': 8.67}, 1: {'Aaditya': 7.7}}
stu = {}

'''
n = int(input("Enter number of students: "))
for i in range(0, n):
    stu = {}
    roll = int(input("Enter the roll number: "))
    name = input("Enter the name of the student: ")
    cpi = float(input("Enter the CPI: "))
    stu[name] = cpi
    stu_db[roll] = stu
'''

from pickle import dump, load
from json import dumps, loads

with open(r"C:\Users\HARSHAL\Desktop\Python\S.Arora 12th std\Ch.5 - File Handling\Binary.dat", 'wb+') as f:
    fpos = f.tell()
    print("Current file pos: ", fpos)

    dump(stu_db, f)

    print("Current file pos: ", f.tell())
    f.seek(-87, 1)
    print("Current file pos: ", f.tell())

    stu = load(f)
    print("Current file pos: ", f.tell())
    print(dumps(stu, indent=4))

    f.seek(-87, 1)
    roll = int(input("Enter the roll number whose data is to be updated: "))
    name,cpi = input("Enter the name") , float(input("Enter the cpi: "))
    stu[roll] = dict({name:cpi})


    f.seek(0,0)
    dump(stu,f)
    f.seek(0,0)
    stu = load(f)
    print("Updated file:- ")
    print(dumps(stu, indent=10))









