"Return the value of the longest contiguous subsequence provided\
the input stops when user inputs -1"
p=int(input("Enter the number: "))
l=0;m_l=0
while p!=-1:
    c=int(input("Enter the number: "))

    if c>p:
        l+=1
    elif c==p:
        if m_l<l:
            m_l=l
        l=1
        #l+=0
    else:
        if m_l<l:
            m_l=l
        l=1
        
    p=c

if m_l<l:
    m_l=l
print(m_l)


        
