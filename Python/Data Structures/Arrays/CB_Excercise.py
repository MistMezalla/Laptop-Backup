def Q1():
    monthly_exp= []

    monthly_exp.append(2200) #Jan
    monthly_exp.append(2350)  # Feb
    monthly_exp.append(2600)  # Mar
    monthly_exp.append(2130) #apr
    monthly_exp.append(2190) #may

    print("Extra in Feb wrt Jan = ",monthly_exp[1]-monthly_exp[0])
    print("First Quarter = ",monthly_exp[0]+monthly_exp[1]+monthly_exp[2])

    print("2000 in any month : ",2000 in monthly_exp)

    monthly_exp.append(1980) #june
    monthly_exp[3] -= 200

    print(monthly_exp)

def Q2():
    marvel_heroes = ["spidey","thor","hulk","iron man","cap america"]

    print(len(marvel_heroes))

    marvel_heroes.append("black panther")
    print(marvel_heroes)

    marvel_heroes.remove("black panther")
    pos = marvel_heroes.index("hulk")
    marvel_heroes.insert(pos+1,"black panther")
    print(marvel_heroes)

    marvel_heroes[1:3] = ["dr strange"]
    print(marvel_heroes)

    marvel_heroes.sort()
    print(marvel_heroes)


Q1()
Q2()
