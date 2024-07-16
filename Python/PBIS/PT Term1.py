dict={'x':11,'y':13,'z':15}
s=""
for i in dict:
    s=s+str(dict[i])+" "
s1=s[:-1]
print(s1[::-1])

def fun(x=10, y=20):
    x+=5
    y = y - 3
    return x*y
print(fun(5),fun())

