# Use of Generators
'''
-> Whenever a normal function gives back value to calling function via the means of "yeild" then that function
name becomes "Generator obj".
->  The yield statement remembers the point where the function last returned a value and resumes from that point the
next time it’s called. This automatic state management makes generators simpler and more concise.
'''
def Fib_Ser():
    a,b = 0,1
    while True:
        yield a
        a,b =b,a+b

Fib_Itr=(Fib_Ser())
for i in range(5):
    print(next(Fib_Itr),end=" ")

print((Fib_Itr),(Fib_Ser()))

def CB_Ex():
    a = 1
    while True:
        yield a*a
        a+=1

sol = CB_Ex()

for num in sol:
    if num > 100:
        break
    print(num, end=" ")



gen_sq = (x*x for x in range(2,10))

print(next(gen_sq))

for val in gen_sq:
    print(val,end= " ")
