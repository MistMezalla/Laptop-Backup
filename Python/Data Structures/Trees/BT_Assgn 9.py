from random import randint
class Tree_node():
    def __init__(self,data,parent = None):
        self.data = data
        self.parent = parent
        self.left = None
        self.right = None

    def add_node(self,data):
        if randint(-10,10)>=0:
            if self.left:
                self.left.add_node(data)
            else:
                self.left = Tree_node(data,self)
        else:
            if self.right:
                self.right.add_node(data)
            else:
                self.right = Tree_node(data,self)
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
    def in_order(self):
        if self.left:
            self.left.in_order()
        print(self.data,end=" ")
        if self.right:
            self.right.in_order()
    def BT_builder_list(self,arr):
        for i in range(len(arr)):
            self.add_node(arr[i])
    def min_BT(self):
        if self.left:
            left_min = self.left.min_BT()
        else:
            left_min = None

        if self.right:
            right_min = self.right.min_BT()
        else:
            right_min= None

        min_node = None
        if left_min:
            if left_min.data < self.data:
                min_node = left_min
            else:
                min_node = self

            if right_min:
                if right_min.data < min_node.data:
                    return right_min
                else:
                    return min_node
        elif right_min:
            if right_min.data < self.data:
                return right_min
            else:
                return self
        else:
            return self

    def min_BT_alt(self):
        #min_val = self.data
        min_node = self

        if self.left:
            left_min = self.left.min_BT_alt()
            if left_min.data<self.data:
                min_node = left_min
            else:
                min_node = self


        if self.right:
            right_min = self.right.min_BT_alt()
            if right_min.data<min_node.data:
                min_node =  right_min

        return min_node

    def max_BT(self):
        max_node = self

        if self.left:
            left_max = self.left.max_BT()
            if left_max.data>max_node.data:
                max_node = left_max

        if self.right:
            right_max = self.right.max_BT()
            if right_max.data > max_node.data:
                max_node = right_max

        return max_node

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

root = Tree_node(10)
l = [14,24,19,0,15,2,7,16]
root.BT_builder_list(l)
root.Print_tree()
print(root.min_BT().data)
#print(root.min_BT_alt().data)
print(root.max_BT().data)
res = root.BT_is_BST()
if not res:
    print("No")
else:
    print("Yes")
print(root.is_BST())
