import threading
import time

'''
-> The blocking introduced by join() ensures that the main thread waits for each thread to complete before moving 
forward in its execution.
-> hence when join() is not part of the code then total time is printed(of the main thread), even though the 
sq_thread and cube_thread didn't finish their resp executions.
-> upon add of join(); statements after join() in the main thread will be exe after the completion of the "joined
threads".
'''
'''
def sq(num: int):
    for i in range(num+1):
        time.sleep(1)
        print("sqr=",i**2)

def cubes(num: int):
    for i in range(num+1):
        time.sleep(0.5)
        print("cube=",i**3)

t = time.time()
num = 5
thr1=threading.Thread(target=sq,args=(num,))
thr2=threading.Thread(target=cubes,args=(num,))

thr1.start()
print("Thread 1 started")
time.sleep(3)
thr2.start()
print("Thread 2 started")
time.sleep(5)
print("A st bet thrd2.start and thrd2.join()")
thr2.join()
print("Thread 2 is joined(i.e. finished exe)")
thr1.join()
print("Thread 1 i joined(i.e. finished exe)")

print(time.time()-t)
'''
def helper():
    for i in range(3):
        print(i)

def CB_Ex():

    for i in range(10):
        thr = threading.Thread(target=helper(), args=())
        thr.start()
        print("Active threads=",threading.active_count())

CB_Ex()

"""
-> A very good program to understand the functioning of the multithreading.
-> Run the program and o/p is self explanaotry
-> However in gist: on each iteration in the for loop a thread is initialised, which upon the start runs in 
concurrent with the main thread. Depending on the time delay set of the "SleepMe()" the new threads will finish the
exe and give the o/p of corresponding thread been awaken.
"""
def sleepMe(i):
    print("Thread %i will sleep." % i)
    time.sleep(0.0001)
    print("Thread %i is awake" % i)

for i in range(10):
    th = threading.Thread(target=sleepMe, args=(i, ))
    print("Thread %i will start" % i)
    th.start()

    print("Current Threads: %i." % threading.active_count())
