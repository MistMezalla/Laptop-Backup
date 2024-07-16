class Tree_node:
    def __init__(self,data,parent = None):
        self.data = data
        self.parent = parent
        self.children = []

    def add_node(self,data: tuple,parent):
        new_node=Tree_node(data,parent)
        new_node.parent.children.append(new_node)
        return new_node

    def get_lvl(self):
        p = self.parent
        lvl = 0
        while p:
            lvl += 1
            p = p.parent

        return lvl
    def print_tree(self,type="both"):
        if type == "name":
            print(" "*self.get_lvl()*4,end="")
            print(self.data[0],end = "\r\n")
            if self.children:
                for child in self.children:
                    child.print_tree("name")

        elif type == "designation":
            print(" " * self.get_lvl() * 4, end="")
            print(self.data[1], end="\r\n")
            if self.children:
                for child in self.children:
                    child.print_tree("designation")

        else:
            print(" " * self.get_lvl() * 4, end="")
            print(f"{self.data[0]} ({self.data[1]})", end="\r\n")
            if self.children:
                for child in self.children:
                    child.print_tree()

    def print_tree_lvl(self,lvl=0):
        curr_lvl = self.get_lvl()
        print(" " * curr_lvl * 4, end="")
        print(self.data[0], end="\r\n")
        if self.children and curr_lvl<lvl:
            for child in self.children:
                child.print_tree_lvl(lvl)



CEO = Tree_node(("Nilupul","CEO"))

CTO = CEO.add_node(("Chinmay","CTO"),CEO)
HR_Head = CEO.add_node(("Gels","HR Head"),CEO)



Infra_Head = CTO.add_node(("Vishwa","Infr Head"),CTO)
CTO.add_node(("aamir","App Head"),CTO)

HR_Head.add_node(("pter","Recu Manager"),HR_Head)
HR_Head.add_node(("waqas","Policy Manager"),HR_Head)

Infra_Head.add_node(("Dahval","App Manager"),Infra_Head)
Infra_Head.add_node(("Abhi","Cloud Manager"),Infra_Head)

CEO.print_tree()
CEO.print_tree("name")
CEO.print_tree("designation")

CEO.print_tree_lvl(2)


