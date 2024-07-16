#Solved Examples
def Ex_28():
    from random import random as rand
    t=rand()*(95-45)+45
    print(t)

    "While using from statement we are't req to prefix the\
    func name of the module"

    from math import ceil
    print(ceil(t))

def Ex_29():
    from random import randint as ri, randrange as rr
    n1,n2=ri(450,950),ri(450,950)
    m1,m2=rr(450,951),rr(450,951)

    print(n1,n2)
    print(m1,m2)
    print(n1,n2,print(m1,m2))
    "Imp: Flow of execution to be noted down in the\
    notebook"   

    from statistics import mean
    "print(mean(n1,n2),mean(m1,m2),sep='&')"

    "mean() takes only one argument\
    hence argument shld be a set or any sequence"

    t1=n1,n2
    t2=m1,m2
    print(mean(t1),mean(t2),sep=' & ')

def Ex_30():
    from random import randrange as rr
    n1=rr(10,70,13)
    n2=rr(10,70,13)    
    n3=rr(10,70,13)
    st={n1,n2,n3}
    print(st)

def Ex_31():
    l=[22,13,28,13,22,25,7,13,25]

    import statistics as st
    print(st.mean(l),\
          st.median(l),\
          st.mode(l),\
          sep='\t')
    
    
Ex_29()

