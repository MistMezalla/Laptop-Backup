num=5

def myFunc():
    #print(num) #In the adjacent statements we can see that since term 'global num' wasn't used hence the value outside the function block is not executed or taken within the function block

    num=10       
    print(num)  

myFunc()
print(num) #Moreover the value num updated within the function remains local even though both local and global terms have same variable and thereby the updated value of num within the function is not executed.

#see the below funtion with the use of prefix global.

t=7

def myfunc():
    global t
    print(t)

    t=10
    print(t)

myfunc()
print(t)
