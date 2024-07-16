dict1={'0':'zero','1':'one','2':'two','3':'three','4':'four','5':'five','6':'six','7':'seven','8':'eight','9':'nine','.':'point'}

num1=float(input('enter the number: '))

for i in str(num1):
   print(dict1.get(i),end=' ')


   
'''
Note:- Number data type (i.e.,float, int,etc) are not iterable
'''

#alternate method
'''
dict2={'0':'zero','1':'one','2':'two',3:'three','4':'four','5':'five','6':'six','7':'seven',8:'eight',9:'nine','.':'point'}

num2=int(input('enter the number: '))

result=''
for i in str(num2):
    key=int(i)
    value=dict2[key]
    result=result+' '+value
    print(result)
'''    

