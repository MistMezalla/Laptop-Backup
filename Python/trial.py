class Tree_node:
    def __init__(self,data,parent = None):
        self.val = data
        self.left = None
        self.right = None
        self.parent = parent
        self.height = 0

    def add_node(self,data):
        if data <= self.val:
            if self.left is None:
                self.left = Tree_node(data,self)
            else:
                self.left = self.left.add_node(data)
        else:
            if self.right is None:
                self.right = Tree_node(data,self)
            else:
                self.right = self.right.add_node(data)

        self.update_height()
        return self.balance()

    def del_node(self,data):
        if data<self.val:
            if self.left:
                self.left = self.left.del_node(data)
            else:
                raise Exception("Value not found")
        elif data>self.val:
            if self.right:
                self.right = self.right.del_node(data)
            else:
                raise Exception("Value not found")
        else:
            if not self.left and not self.right:
                return None
            elif not self.left:
                self.right.parent = self.parent
                return self.right
            elif not self.right:
                self.left.parent = self.parent
                return self.left

            pre = self.left.max_node()
            self.val = pre.val
            self.left = self.left.del_node(pre.val)

        self.update_height()
        return self.balance()
    def max_node(self):
        node = self
        while node.right:
            node = node.right

        return node

    def update_height(self):
        left_height = self.left.height if self.left else -1
        right_height = self.right.height if self.right else -1

        self.height = max(left_height,right_height) + 1

    def bf(self):
        left_height = self.left.height if self.left else -1
        right_height = self.right.height if self.right else -1

        return left_height - right_height

    def right_rotate(self):
        x = self
        y = x.left
        t2 = y.right

        y.right = x

        if t2:
            t2.parent = x

        y.parent = x.parent
        x.left = t2
        x.parent = y

        x.update_height()
        y.update_height()

        return y

    def left_rotate(self):
        x = self
        y = x.right
        t2 = y.left

        y.left = x

        if t2:
            t2.parent = x

        y.parent = x.parent
        x.right = t2
        x.parent = y

        x.update_height()
        y.update_height()

        return y

    def balance(self):
        self.update_height()
        bal_fact = self.bf()

        if bal_fact > 1:
            if self.left and self.left.bf() >= 0:
                return self.right_rotate()
            else:
                self.left = self.left.left_rotate()
                return self.right_rotate()

        elif bal_fact < -1:
            if self.right and self.right.bf() <= 0:
                return self.left_rotate()
            else:
                self.right = self.right.right_rotate()
                return self.left_rotate()

        return self

    def bfs(self):
        levels = []
        current_lvl = [self]

        while any(current_lvl):
            levels.append(current_lvl)
            next_lvl = []
            for node in current_lvl:
                if node is None:
                    next_lvl = [None, None]
                else:
                    next_lvl.append(node.left)
                    next_lvl.append(node.right)
            current_lvl = next_lvl
        return levels

    def print_tree(self):
        levels = self.bfs()
        max_lvl = len(levels) - 1
        max_width = (2**max_lvl) * 5

        for i,level in enumerate(levels):
            line = ""
            sp = max_width//(2**i)
            bet_sp = max_width//(2**(i+1))

            for j,node in enumerate(level):
                if j == 0:
                    line += " " * (sp//2)
                else:
                    line += " " * bet_sp
                if node is None:
                    line += " " * 4
                else:
                    line += f"{node.val:4}"

            print(line.rstrip())
            print()

    def in_order(self):
        if self.left:
            self.left.in_order()
        print(self.val, end=" ")
        if self.right:
            self.right.in_order()
    def AVL_Build_list(self,nums):
        root = self
        for data in nums:
            root = root.add_node(data)
            while root.parent:
                root = root.parent
        return root




root = Tree_node(10)
elem = [9, 8, 7, 6, 15, 4, 2, 19, 16, 17, 12, 13, 11, 18, 20, 25, 22, 23, 27, 29]
root = root.AVL_Build_list(elem)
root.print_tree()
root.in_order()
print()

root = root.del_node(12)
root.print_tree()
root.in_order()
print()



