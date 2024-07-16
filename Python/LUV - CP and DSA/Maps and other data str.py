# Maps of C++
from sortedcontainers import SortedDict
def sorteddict_implementation():
    m = SortedDict(zip((3,4,2,1),("a","d","c")))
    print(m)

# Mutlimaps of C++
from collections import defaultdict
def defaultdict_implementation():
    m = defaultdict(list)
    m[1].append("a")
    m[2].append("a")
    m[0].append("d")
    m[1].append("b")

    print(m)

from collections import Counter
def Counter_implementation():
    '''
    cntr = Counter([4,3,1,2,4,2,3,3,1,4])
    print(cntr)

    list = sorted(cntr)
    print(list)

    print(cntr.elements())
    print(cntr)
    mc = (cntr.most_common())
    print(mc)
    '''
    word = "ddddbb"
    cntr = Counter(word)
    print(cntr)




#sorteddict_implementation()
#defaultdict_implementation()
Counter_implementation()


