f=open("story.txt","r")
l=f.readlines()
for line in l:
    w=line.split()
    for word in w:
        print(word+"#",end="")
    print("")
f.close()
