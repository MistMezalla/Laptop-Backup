'''
-> In order to return pointer here an obj(or ref) hence __iter__ "returns self"
-> In other words __iter__ makes the function as iterator obj else __next__ will be invalid for usage
-> In the below code __iter__ is called implicitly to make the Fib_Ser class instances an iterator.
'''

def Iter_Ex():
    class Fib_Ser():
        def __init__(self,limit: int):
            self.prev = 0
            self.curr = 1
            self.cnt = 1
            self.limit = limit

        def __iter__(self):
            return self

        def __next__(self):
            if self.cnt == 1:
                self.cnt+=1
                return self.prev
            elif self.cnt == 2:
                self.cnt += 1
                return self.curr
            elif self.cnt < self.limit:
                res = self.curr + self.prev
                self.prev = self.curr
                self.curr=res
                self.cnt += 1
                return res
            else:
                raise Exception("Limit Reached")


    Fib_itr=Fib_Ser(12)

    print((type(Fib_itr)))
    for val in Fib_itr:
        print(val,end=" ")
    '''
    while True:
        try:
            print(next(Fib_itr),end=" ")
        except StopIteration:
            break
    '''

Iter_Ex()

'''
-> However the iterator can be called explicitly in the abv code as follows:-
Fib_itr = Fib_Ser(12)
    
# Explicitly calling __iter__
iter_obj = Fib_itr.__iter__()

-> While you usually don't need to call __iter__ explicitly (because it’s handled by iteration constructs like for
loops), you can do so if needed.   
-> In the context of your code, calling __iter__ explicitly doesn’t change the functionality because the method just 
returns self.
-> Explicitly calling __iter__ can be useful in cases where you want to reset the iteration or when dealing with 
objects where __iter__ returns something other than self.
'''