def myMean(list1):
    total=0
    
    for i in list1:
        total+=i
        count=len(list1)
        mean=total/count
    print(mean)
        
list1=[1.1,2.2,3.3,4.4,5.5,6.6,7.7]
myMean(list1)
        
