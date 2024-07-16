import time
'''
-> *args => pos arguments
-> *kwargs => key word arguments
-> if *args is missing in the wrapper function then:-
func call: sq_in_range(1, 10)
error :-
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
TypeError: wrapper() takes 0 positional arguments but 2 were given
-> If **kwargs is missing:-
function call: sq_in_range(st=1, end=10)
error:-
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
TypeError: wrapper() got an unexpected keyword argument 'st'
'''
def time_it(func):
    def wrapper(*args,**kwargs):
        start = time.time()
        res = func(*args,**kwargs)
        end = time.time()
        print(f"{func.__name__} : {(end-start)*1000} ms")
        return res
    return wrapper

@time_it
def sq_in_range(st: int,end: int):
    for i in range(st,end+1):
        print(i**2,end=" ")
    print()

    return [i*i for i in range(st,end+1)]

def is_pos(f):
    def wrapper(*args,**kwargs):
        if args[0] < 0 and type(args[0]) == int:
            raise TypeError("Enter int type to find the factorial")
        return f(*args, **kwargs)
    return wrapper

'''
-> The *args store the values as tuple: args = ()
-> **kwargs store as dictionary : kwargs = {}
'''
@is_pos
def CB_Ex(num):
    res = 1
    if num == 0:
        return res
    else:
        for i in range(num,0,-1):
            res*=i
        return res

#sq_in_range(1,10)
print(CB_Ex(5))
print(CB_Ex(-5))