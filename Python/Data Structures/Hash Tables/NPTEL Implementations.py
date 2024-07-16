def Horner_Rule(nums: list[int]):
    p=0
    for i in range(len(nums)-1,-1,-1):
        p = nums[i] + 37*p

    return p

from math import floor,sqrt
class HashTable():
    def __init__(self):
        self.MAX = 10
        self.arr = [None for i in range(self.MAX)]

    def get_hash(self,key):
        res = [ord(elem) for elem in key]
        A=(sqrt(5)-1)/2
        return floor(self.MAX*(Horner_Rule(res)*A%1))

    def prob_range(self,index):
        return [*range(index,self.MAX)]+[*range(0,index)]

    # range(index, self.MAX): This creates a range object starting from index and ending at self.MAX - 1.
    # The asterisk * is used for unpacking the range objects into lists.

    def find_slot(self,key,index):
        ran = self.prob_range(index)

        for ind in ran:
            if self.arr[ind] == None:
                return ind
            elif self.arr[ind][0] == key:
                return ind

        raise Exception("Hash Table is Full")

    def ins_slot(self,key,index):
        ran = self.prob_range(index)

        for ind in ran:
            if self.arr[ind] == None:
                return ind
            elif self.arr[ind] == [None]:
                return ind
            elif self.arr[ind][0] == key:
                return ind

        raise Exception("Hash Table is Full")


    def __setitem__(self, key, value):
        h=self.get_hash(key)

        if self.arr[h] == None:
            self.arr[h] = (key,value)
        else:
            self.arr[self.ins_slot(key, h)] = (key,value)

    def __getitem__(self,key):
        h=self.get_hash(key)

        if self.arr[h] == None:
            return self.arr[h]
        else:
            if self.arr[self.find_slot(key,h)] == None:
                return None
            return self.arr[self.find_slot(key,h)][1]

    def __delitem__(self, key):
        h = self.get_hash(key)

        if self.arr[h] == None:
            return self.arr[h]
        else:
            self.arr[self.find_slot(key,h)]=[None] #[None] is the tombstone marker



dic = HashTable()
print(dic.arr)
dic["Jan 1"] = 25
print(dic.arr)
print(dic["Jan 1"])
dic["naJ 1"] = 27
print(dic.arr)
dic["Jan 2"]=30
dic["Jan 3"]=29
dic["Jan 4"]=22
dic["Jan 5"]=24
dic["Jan 6"]=22
dic["Jan 7"]=25
dic["Jan 2"]=28
print(dic.arr)
print(dic["Jan 7"])
del dic["Jan 6"]
print(dic.arr)
print(dic["Jan 7"])
dic["Jan 6"] = 20
print(dic.arr)