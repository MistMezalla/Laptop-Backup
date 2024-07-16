'''
-> The below code as potential errors wrt T(n) and deletion of node with 2 children
    -> The below code fails to handle the case of del of node of 2 children as the balancing logic for rest case
    doesn't go with this case

    -> In the worst case scenarios the order of operations for insertion and deletion go up to O(n) as the bf()
    calculates height of tree in its every call
'''
class AVL_Tree_node:
    def __init__(self,data,parent = None):
        self.data = data
        self.parent = parent
        self.left = None
        self.right = None

    def add_node(self,data):
        if data <= self.data:
            if self.left == None:
                self.left = AVL_Tree_node(data,self)
            else:
                self.left.add_node(data)
        else:
            if self.right == None:
                self.right = AVL_Tree_node(data,self)
            else:
                self.right.add_node(data)

        return self.balance()

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

            pre = self.left.max_node()
            self.data = pre.data
            self.left = self.left.del_node(pre.data)

        x = self.parent
        y = self
        bf_y = y.bf()
        if bf_y > 1:
            y = y.left
            return y.balance()
        elif bf_y < -1:
            y = y.right
            return y.balance()

        return y

    def max_node(self):
        if not self.right:
            return self

        return self.right.max_node()


    def height_tree(self):
        if not self.left and not self.right:
            return 1

        left_height = right_height = 0
        if self.left:
            left_height = self.left.height_tree()

        if self.right:
            right_height = self.right.height_tree()

        return max(left_height,right_height) + 1

    def right_rotate(self):
        x = self.parent
        y = self

        y.parent = x.parent
        if y.right:
            y.right.parent = x
        x.left = y.right
        if x.parent:
            if x.parent.left == x:
                x.parent.left = y
            else:
                x.parent.right = y
        x.parent = y
        y.right = x

        return y

    def left_rotate(self):
        x = self.parent
        y = self

        y.parent = x.parent
        if y.left:
            y.left.parent = x
        x.right = y.left
        if x.parent:
            if x.parent.left == x:
                x.parent.left = y
            else:
                x.parent.right = y
        x.parent = y
        y.left = x

        return y

    def bf(self):

        left_height = right_height = 0
        if self.left:
            left_height = self.left.height_tree()

        if self.right:
            right_height = self.right.height_tree()

        return left_height - right_height

    def balance(self):
        x = self.parent
        y = self

        if x is None:
            return y

        bf = x.bf()

        if bf > 1:
            if y == x.left:
                if y.left:
                    return y.right_rotate()

                else: #LR case
                    y = y.right.left_rotate()
                    return y.right_rotate()

        elif bf < -1:
            if y == x.right:
                if y.right:
                    return y.left_rotate()

                else:  # LR case
                    y = y.left.right_rotate()
                    return y.left_rotate()

        return y

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

        print(self.data,end = " ")

        if self.right:
            self.right.in_order()

    def AVL_Build_list(self,arr):
        root = self
        for data in arr:
            root = root.add_node(data)
            while root.parent:
                root = root.parent
        return root

root = AVL_Tree_node(10)
elem = [9,8,7,6,15,4,2,19,16,17,12,13,11,18,20,25,22,23,27,29]
root = root.AVL_Build_list(elem)
root.Print_tree()
root.in_order()
print()
'''
root = root.del_node(12)
root.Print_tree()
root.in_order()
print()
'''
'''
root1 = AVL_Tree_node(20)
elem1 = [10,15,25,22]
root1 = root1.AVL_Build_list(elem1)
root1.Print_tree()
root1.in_order()
print()
'''

