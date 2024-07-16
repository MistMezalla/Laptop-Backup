#import time module
import time

#define countdown func.
def  countdown(t):
    while t:
        mins,secs =divmod(t,60)
        timer ='{:02d}:{:02d}'.format(mins,secs)
        print(timer,end='\n')
        time.sleep(1)
        t-=1

    print('Fire in the hole!')

#input time in seconds
t=input('enter the time in seconds: ')

#functional call
countdown(int(t))
