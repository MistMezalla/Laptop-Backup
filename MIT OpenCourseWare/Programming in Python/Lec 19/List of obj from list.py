class Animal(object):
    def __init__(self, age):
        self.age = age
        self.name = None

    def __str__(self):
        return 'Name: ' + str(self.name) + '\tand\tAge: ' + str(self.age)

    def set_name(self, name=" "):
        self.name = name


L1 = [2, 5, 1]
L2 = ["Fish", "Cat", "Dog"]

L = []

for i in range(0, len(L1)):
    #L[i] = Animal(L1[i])
    '''
    The list L is initialized as an empty list, and you're trying to assign values to specific indices in it 
    directly (L[i]). This will raise an IndexError because the list doesn't have any elements initially.
    Solution: Use L.append() to add elements to the list.
    '''
    L.append(Animal(L1[i]))
    L[i].set_name(L2[i])

# print(L)
for item in L:
    print(f'{item}')

