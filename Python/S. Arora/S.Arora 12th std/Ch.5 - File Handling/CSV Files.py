import csv
stu_db = {89: {'Harshal': 9.0}, 101: {'Junaid': 8.67}, 1: {'Aaditya': 7.7}}
with open(r'C:\Users\HARSHAL\Desktop\Python\S.Arora 12th std\Ch.5 - File Handling\Student.csv','w+',newline='') as f:
    fw=csv.writer(f)
    fw.writerow(["Roll No","Name","CPI"])
    for roll in stu_db.keys():
        name = list(stu_db[roll].keys())[0]
        cpi = stu_db[roll][name]
        fw.writerow([roll, name, cpi])

    print(f.tell())
    f.seek(0,0)
    fr=csv.reader(f)
    for rec in fr:
        print(rec)



