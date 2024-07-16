import csv
def Q1():
    l=[]
    with open(r"C:\Users\HARSHAL\Desktop\Python\Data Structures\Hash Tables\nyc_weather.csv", 'r', newline='') as f:
        fr=csv.reader(f)

        for ind,row in enumerate(fr):
            if(ind==0):
                continue
            l.append(int(row[1]))

        print(f"{sum(l[:7])/len(l[:7]):.2f}")
        print(max(l))

def Q2():
    d={}
    with open(r"C:\Users\HARSHAL\Desktop\Python\Data Structures\Hash Tables\nyc_weather.csv", 'r', newline='') as f:
        fr=csv.reader(f)

        for ind,row in enumerate(fr):
            if(ind == 0):
                continue
            d[row[0]]=int(row[1])

        print(d['Jan 9'],d['Jan 4'])

def Q3():
    d={}
    with open(r"C:\Users\HARSHAL\Desktop\Python\Data Structures\Hash Tables\poem(my mother at sixty six).txt", 'r', newline='') as f:
       for elem in f.readlines():
           for word in (elem.strip()).split(" "):
               if word in d:
                   d[word]+=1
               else:
                   d[word]=1

    for key in d:
        print(f"{key} : {d[key]}")

#Hash Map using Linear Probing
def Q4():
    class HashMap:
        def __init__(self):
            self.MAX = 5
            self.arr = [[None,None] for i in range(5)]

        def get_hash(self,key):
            sum = 0
            for char in key:
                sum+=ord(char)

            return sum%self.MAX

        def __setitem__(self, key, value):
            H = self.get_hash(key)
            h = H

            found = False
            elem = self.arr[h]
            if elem[0] == key:
                elem[1] = value
                found = True
            elif elem[0] == None:
                self.arr[h][:2]=[key,value]
                found = True
            else:
                h = (h + 1) % self.MAX

            while h!=H and not found:
                elem = self.arr[h]
                if elem[0]==key:
                    elem[1]=value
                    found = True
                elif elem[0]==None:
                    self.arr[h][:2] = [key, value]
                    found = True
                else:
                    h=(h+1)%self.MAX

            if not found:
                print("Hash Table is full")

        def __getitem__(self, key):
            H = self.get_hash(key)
            h = H

            if self.arr[h][0] == key:
                return self.arr[h][1]
            elif self.arr[h][0] == None:
                return "Elem not found"
            else:
                h = (h+1)%self.MAX

            while h!=H:
                if self.arr[h][0] == key:
                    return self.arr[h][1]
                elif self.arr[h][0] == None:
                    return "Elem not found"
                else:
                    h = (h + 1) % self.MAX

        def __delitem__(self, key):
            H = self.get_hash(key)
            h = H

            found = False
            if self.arr[h][0] == key:
               self.arr[h][:2]=[None,None]
               found = True
            else:
                h = (h + 1) % self.MAX

            while h != H and not found:
                if self.arr[h][0] == key:
                    self.arr[h][:2] = [None, None]
                    found = True
                else:
                    h = (h + 1) % self.MAX

            if not found:
                raise Exception ("Value not found")


    Linear_Hash = HashMap()
    print(Linear_Hash.arr)
    Linear_Hash["Jan 1"]=30
    Linear_Hash["Jan 2"]=33
    Linear_Hash["Jan 3"]=30
    print((Linear_Hash.arr))
    Linear_Hash["naJ 1"]=35
    print((Linear_Hash.arr))
    Linear_Hash["naJ 3"]=37
    print(Linear_Hash.arr)
    print(Linear_Hash["Jan 1"])
    print(Linear_Hash["naJ 3"])
    del Linear_Hash["naJ 1"]
    print(Linear_Hash.arr)

def Q4_sol():
    class HashTable:
        def __init__(self):
            self.MAX = 5  # I am keeping size very low to demonstrate linear probing easily but usually the size should be high
            self.arr = [None for i in range(self.MAX)]

        def get_hash(self, key):
            hash = 0
            for char in key:
                hash += ord(char)
            return hash % self.MAX

        def __getitem__(self, key):
            h = self.get_hash(key)
            if self.arr[h] is None:
                return
            prob_range = self.get_prob_range(h)
            for prob_index in prob_range:
                element = self.arr[prob_index]
                if element is None:
                    return
                if element[0] == key:
                    return element[1]

        def __setitem__(self, key, val):
            h = self.get_hash(key)
            if self.arr[h] is None:
                self.arr[h] = (key, val)
            else:
                new_h = self.find_slot(key, h)
                self.arr[new_h] = (key, val)
            print(self.arr)

        def get_prob_range(self, index):
            return [*range(index, len(self.arr))] + [*range(0, index)]

        def find_slot(self, key, index):
            prob_range = self.get_prob_range(index)
            for prob_index in prob_range:
                if self.arr[prob_index] is None:
                    return prob_index
                if self.arr[prob_index][0] == key:
                    return prob_index
            raise Exception("Hashmap full")

        def __delitem__(self, key):
            h = self.get_hash(key)
            prob_range = self.get_prob_range(h)
            for prob_index in prob_range:
                if self.arr[prob_index] is None:
                    return  # item not found so return. You can also throw exception
                if self.arr[prob_index][0] == key:
                    self.arr[prob_index] = None
            print(self.arr)

    dic = HashTable()
    print(dic.arr)
    dic["Jan 1"]=35
    '''
    dic["naJ 1"]=37
    dic["Jan 2"]=34
    dic["Jan 3"]=30
    print(dic.arr)
    '''

#Q4()
Q4_sol()
