#1.String Literals

#1.1. Some Backslash Func and its uses
def Backslash_Func():
    st1='Hello Everyone\tGood Morning'
    st2='Hello Everyone\nGood Morning'
    print(st1,st2)
    print(st1,st2,sep='#')

#1.2. Multiline strings
def Multiline_String():
    st3='Hello Everyone\
Good Morning'
    st4='''Hello Everyone
Good Morning'''
    st5="""Hello Everyone
Good Morning"""
    print(st3,st4,st5,sep='\n')
    print(len(st3),len(st4),len(st5))

#Note:-
'The len func takes exactly one argument'

print(10+12,end='@'); print(10*12)

#Note:-
'So ; is kind of analogously similar to \ in case of multiline string'






