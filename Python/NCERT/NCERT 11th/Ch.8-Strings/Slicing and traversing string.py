#slicing and traversing string

str='Harshal Sanas'

print(str[0:13])
print(str[-1:-13:-2])

for letter in str:
    print(letter,end='')
print()
#the empty print has by default end=\n, hence when this wasn.t there the cursor hadn't shift to next line as in the abv print statement end='', thereby there is no instruction given to python to shift to next line. this instruction of shifting to nextline is given by print() statement.


index=0
while index<len(str):
    print(str[index],end='')
    index+=1
