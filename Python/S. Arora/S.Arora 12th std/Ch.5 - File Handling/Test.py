with open(r'C:\Users\HARSHAL\Desktop\Python\S.Arora 12th std\Ch.5 - File Handling\carriage ret.txt','w+') as f:
    print(f.tell())
    f.write("First Line\r\nSecond Line")
    print(f.tell())
    f.seek(0,0)
    print(f.read(11))
    print(f.tell())
