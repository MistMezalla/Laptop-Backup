class Animal(object):
    def __init__(self, age):
        self.age = age
        self.name = None

    def __str__(self):
        return 'Animal\'s Name: ' + str(self.name) + '\tand\tAge: ' + str(self.age)

    def set_name(self, name):
        self.name = name


class Cat(Animal):
    def __str__(self):
        return 'Cat\'s Name: ' + str(self.name) + '\tand\tAge: ' + str(self.age)


class Person(Animal):
    def __init__(self, age, name):
        Animal.__init__(self, age)
        self.set_name(name)

    def __str__(self):
        return 'Person\'s Name: ' + str(self.name) + '\tand\tAge: ' + str(self.age)


People_name = ["Ana", "Bella"]
People_age = (21, 27)
Pets = (5, 3)
Pets_name = ["Fluffy", "Murphy"]
L_Pets = []
L_People = []

for i in range(len(Pets)):
    L_Pets.append(Cat(Pets[i]))
    L_Pets[i].set_name(Pets_name[i])

for i in range(len(People_name)):
    L_People.append(Person(People_age[i], People_name[i]))

d = {}
for i in range(len(L_People)):
    d[L_People[i]] = L_Pets[i]

for k, v in d.items():
    print(f'{k} and it\'s {v}')














