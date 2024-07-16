L=eval(input('Enter list values')) 
length=len(L) #length=6 
min=L[0] #min=10 
loc=-1 
for i in range(length): #0,1,2,3,4,5 
    if L[i]<min: 
        min=L[i] #min=1 
        loc=i 
print("Minimum value=",min) 
print("Location=",loc)
