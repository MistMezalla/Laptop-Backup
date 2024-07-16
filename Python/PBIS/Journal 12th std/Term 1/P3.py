file=open("test.txt","r")
lines=file.readlines()
print(lines)
file.close()

file=open("test.txt","w")
file1=open("test2.txt","w")
for line in lines:
    if 'a' in line:
        file1.write(line)
    else:
        file.write(line)
print("All lines that contain a character has been moved in test2.txt file")
file.close()
file1.close()

file2=open("test.txt","r")
t=file2.read()
print(t)
file2.close()

file3=open('test2.txt','r')
m=file3.read()
print(m)
file3.close()

