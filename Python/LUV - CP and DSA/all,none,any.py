from sortedcontainers import SortedList

multiset = SortedList()
multiset.add(8)
multiset.add(-7)
multiset.add(20)
multiset.add(12)
multiset.add(-3)

print(multiset)

print(all(x>=0 for x in multiset))
print(any(x>=0 for x in multiset))
print(not any(x>=0 for x in multiset))