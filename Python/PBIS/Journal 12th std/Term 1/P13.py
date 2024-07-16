aDict={'Bhavna':1,"Richard":2,"Firoza":3,"Arshnoor":4}
val=eval(input('Enter value')) 
flag=0 
for k in aDict: 
    if val==aDict[k]: 
        print("value found at key",k) 
        flag=1 
    if flag==0: 
        print("value not found")
