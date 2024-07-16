# Chaining Based Hash Table
class Hash_Table:
    def __init__(self):
        self.MAX = 10
        self.arr = [[] for i in range(10)]

    def get_hash(self,key):
        key = str(key)
        hash = 0
        for char in key:
            hash+=ord(char)

        return hash%self.MAX

    def __getitem__(self, key):
        h = self.get_hash(key)
        for ind, elem in enumerate(self.arr[h]):
            if elem[0] == key:
                return self.arr[h][ind][1]

    def __setitem__(self, key, value):
        h = self.get_hash(key)

        found = False
        for ind,elem in enumerate(self.arr[h]):
            if len(elem) == 2 and elem[0]==key:
                self.arr[h][ind][1] = value
                found = True
                break
        if not found:
            self.arr[h].append((key,value))


    def __delitem__(self, key):
        h = self.get_hash(key)

        for ind,elem in enumerate(self.arr[h]):
            if elem[0] == key:
               del self.arr[h][ind]


dic = Hash_Table()
dic[10] = 'a'
dic['a']="Siuuu"
print(dic.arr)
print(dic[10],dic['a'])
dic[11]='b'
dic['b']='Asi Asi Asi Gana el Madrid'
print(dic.arr)
#del dic[11]
#del dic['a']
print(dic.arr)

