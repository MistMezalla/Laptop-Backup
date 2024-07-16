class Tree_node():
    def __init__(self,data,parent=None):
        self.data =  data
        self.parent = parent
        self.left = None
        self.right = None

    def add_node(self,data):
        if data <= self.data :
            if self.left == None:
                self.left = Tree_node(data,self)
            else:
                self.left.add_node(data)
        else:
            if self.right == None:
                self.right = Tree_node(data,self)
            else:
                self.right.add_node(data)

    def add_node_iter(self,data):
        root = self
        while root:
            if data<= root.data:
                if not root.left:
                    root.left = Tree_node(data,root)
                    break
                else:
                    root = root.left
            else:
                if not root.right:
                    root.right = Tree_node(data,root)
                    break
                else:
                    root = root.right


    def BST_bulider_list(self,arr: list[int]):
        for i in range(len(arr)):
            self.add_node_iter(arr[i])

    def get_lvl(self):
        lvl = 0
        p = self.parent

        while p:
            lvl += 1
            p = p.parent

        return lvl

    def in_order(self):
        if self.left:
            self.left.in_order()
        print(self.data,end=" ")
        if self.right:
            self.right.in_order()

    def pre_order(self):
        if self:
            print(self.data, end=" ")
            self.left.in_order()
            self.right.in_order()

    def post_order(self):
        if self:
            self.left.in_order()
            self.right.in_order()
            print(self.data, end=" ")

    def print_tree(self):
        print(" "*self.get_lvl()*4,end="")
        print(self.data,end="\r\n")
        if self.left:
            self.left.print_tree()
        if self.right:
            self.right.print_tree()

    def Print_tree(self):
        levels = self.get_tree_levels()
        max_level = len(levels) - 1
        max_width = (2 ** max_level) * 4  # Maximum width for the last level

        for i, level in enumerate(levels):
            line = ""
            spacing = max_width // (2 ** i)
            between_spacing = max_width // (2 ** (i + 1))
            for j, node in enumerate(level):
                if j == 0:
                    line += " " * (spacing // 2)
                else:
                    line += " " * between_spacing
                if node is None:
                    line += " " * 4  # Placeholder for None nodes
                else:
                    line += f"{node.data:4}"
            print(line.rstrip())
            print("\n")

    def get_tree_levels(self):
        levels = []
        current_level = [self]
        while any(current_level):
            levels.append(current_level)
            next_level = []
            for node in current_level:
                if node is None:
                    next_level.extend([None, None])
                else:
                    next_level.append(node.left)
                    next_level.append(node.right)
            current_level = next_level
        return levels

    def min(self):
        if self.left:
            return self.left.min()
        else:
            return self

    def max(self):
        if self.right:
            return self.right.max()
        else:
            return self

    def search(self,data):
        if data == self.data:
            return self
        if data < self.data:
            if self.left:
                return self.left.search(data)
            else:
                return None
        else:
            if self.right:
                return self.right.search(data)
            else:
                return None

    def del_node(self,data):
        if data < self.data:
            if self.left:
                self.left = self.left.del_node(data)
            else:
                raise Exception ("Value not found")
        elif data > self.data:
            if self.right:
                self.right = self.right.del_node(data)
            else:
                raise Exception ("Value not found")
        else:
            if not self.left and not self.right:
                return None
            elif not self.right:
                self.left.parent = self.parent
                return self.left
            elif not self.left:
                self.right.parent = self.parent
                return self.right


            pre = self.left.max()
            self.data = pre.data
            self.left.del_node(pre.data)

        return self

    def BT_is_BST(self):
        node = self

        if self.left:
            left_node = self.left.BT_is_BST()
            if not left_node:
                return False
            if left_node.data>node.data:
                return False

        if self.right:
            right_node = self.right.BT_is_BST()
            if not right_node:
                return False
            if right_node.data<node.data:
                return False

        return node

    def is_BST(self):
        def helper(node,min_val,max_val):
            if not node:
                return True
            elif not (min_val<=node.data<=max_val):
                return False

            return helper(node.left,min_val,node.data) and helper(node.right,node.data,max_val)

        return helper(self,float("-inf"),float("inf"))


'''
root = Tree_node(10)
root.BST_bulider_list([8,7,7.5,12,9,5,11,13,16,14])
root.Print_tree()
root.in_order()
min_node = root.min()
print()
print(min_node.data)
print(root.min().data)
max_node = root.max()
print(max_node.data)
search_node = root.search(16)
if search_node:
    print(f"Found {search_node.data}")
else:
    print("Not found")
root.del_node(8)
root.Print_tree()
res = root.BT_is_BST()
if not res:
    print("No")
else:
    print("Yes")
print(root.is_BST())
'''
root1 = Tree_node(10)
root1.BST_bulider_list([20,3,4,5,8,7,12,13,15])
root1.Print_tree()
root1.in_order()
print()

root1 = root1.del_node(10)
root1.Print_tree()
root1.in_order()
print()