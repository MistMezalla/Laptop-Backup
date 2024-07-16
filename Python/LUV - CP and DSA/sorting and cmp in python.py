l1 = [-3,-4,2,1,8,0,9,4,-1,-2,3]
'''
The sort(key = None, reverse  =  False)
-> The key has same ana usage as cmp in c++
-> Some of the uses of key are giv below 
'''
# key = abs
l1.sort(key =abs)
print(l1)
'''
-> The key=abs sorts the list by the absolute value of each element, which means that the order of elements is 
determined by their distance from zero, ignoring their sign.
'''

# key = len and case insensitive(for strings)
l2 = ["Banana", "aPple", "CheRry", "Date","date","Mango"]
l2.sort(key = len)
print(l2)

l3 = ["Banana", "aPple", "CheRry", "Date","date","Mango"]
l3.sort(key = lambda word: word.lower())
print(l3)

# pair
l4 = [
    {'name': 'John', 'grade': 90, 'age': 18},
    {'name': 'Jane', 'grade': 92, 'age': 17},
    {'name': 'Dave', 'grade': 90, 'age': 17}
]

l4.sort(key = lambda pair: (pair["grade"],pair["age"]))
print(l4)