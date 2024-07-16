str1='''He
ll
o''' #'\n' is included in this case in the size of the string.

str2="He\
ll\
o"

print(str1,str2,sep='\t')
print(len(str1),len(str2))
