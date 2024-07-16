class Tree_node:
    def __init__(self,data,parent=None):
        self.data = data
        self.parent = parent
        self.children = []

    def get_lvl(self):
        lvl=0
        p = self.parent
        while p:
            lvl+=1
            p = p.parent

        return lvl

    def add_node(self,data,parent):
        new_node = Tree_node(data,parent)
        new_node.parent.children.append(new_node)
        return new_node  # Return the newly created node to add children to it later

    def print_tree(self):
        print(" "*self.get_lvl()*4,end="")
        print(self.data,end = "\r\n")
        if self.children:
            for child in self.children:
                child.print_tree()


root = Tree_node("Electronics")

Laptop = root.add_node("Laptops",root)
TV = root.add_node("TV",root)
Mobiles = root.add_node("Mobiles",root)


Laptop.add_node("Mac",Laptop)
Laptop.add_node("HP",Laptop)
Laptop.add_node("Dell",Laptop)

TV.add_node("Samsung",TV)
TV.add_node("LG",TV)

Mobiles.add_node("iPhone",Mobiles)
Mobiles.add_node("Vivo",Mobiles)
Mobiles.add_node("Xiaomi",Mobiles)
Mobiles.add_node("Oppo",Mobiles)

root.print_tree()
