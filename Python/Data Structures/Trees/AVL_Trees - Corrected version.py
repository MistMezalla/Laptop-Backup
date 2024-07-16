class AVL_Tree_node:
    def __init__(self, data, parent=None):
        self.data = data
        self.parent = parent
        self.left = None
        self.right = None
        self.height = 1  # Add height attribute

    def add_node(self, data):
        if data <= self.data:
            if self.left is None:
                self.left = AVL_Tree_node(data, self)
            else:
                self.left = self.left.add_node(data)
        else:
            if self.right is None:
                self.right = AVL_Tree_node(data, self)
            else:
                self.right = self.right.add_node(data)

        self.update_height()  # Update height after insertion
        return self.balance()

    def del_node(self, data):
        if data < self.data:
            if self.left:
                self.left = self.left.del_node(data)
            else:
                raise Exception("Value not found")
        elif data > self.data:
            if self.right:
                self.right = self.right.del_node(data)
            else:
                raise Exception("Value not found")
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
            self.left = self.left.del_node(pre.data)  # Update structure correctly

        self.update_height()  # Update height after deletion
        return self.balance()

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

        return max(left_height, right_height) + 1

    def right_rotate(self):  # Update right_rotate method
        y = self
        x = y.left
        t2 = x.right

        x.right = y
        y.left = t2

        if t2:
            t2.parent = y

        x.parent = y.parent
        y.parent = x

        y.update_height()  # Update height of y after rotation
        x.update_height()  # Update height of x after rotation

        return x

    def left_rotate(self):  # Update left_rotate method
        y = self
        x = y.right
        t2 = x.left

        x.left = y
        y.right = t2

        if t2:
            t2.parent = y

        x.parent = y.parent
        y.parent = x

        y.update_height()  # Update height of y after rotation
        x.update_height()  # Update height of x after rotation

        return x

    def bf(self):
        left_height = self.left.height if self.left else 0  # Use height attribute
        right_height = self.right.height if self.right else 0  # Use height attribute
        return left_height - right_height

    def update_height(self):  # New method to update height
        left_height = self.left.height if self.left else 0
        right_height = self.right.height if self.right else 0
        self.height = max(left_height, right_height) + 1

    def balance(self):
        self.update_height()  # Ensure height is updated before balancing
        balance_factor = self.bf()

        if balance_factor > 1:
            if self.left and self.left.bf() >= 0:
                return self.right_rotate()
            else:
                self.left = self.left.left_rotate()
                return self.right_rotate()

        if balance_factor < -1:
            if self.right and self.right.bf() <= 0:
                return self.left_rotate()
            else:
                self.right = self.right.right_rotate()
                return self.left_rotate()

        return self

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
        print(self.data, end=" ")
        if self.right:
            self.right.in_order()

    def AVL_Build_list(self, arr):
        root = self
        for data in arr:
            root = root.add_node(data)
            while root.parent:
                root = root.parent
        return root

# Testing the updated AVL tree implementation
root = AVL_Tree_node(10)
elem = [9, 8, 7, 6, 15, 4, 2, 19, 16, 17, 12, 13, 11, 18, 20, 25, 22, 23, 27, 29]
root = root.AVL_Build_list(elem)
root.Print_tree()
root.in_order()
print()

root = root.del_node(12)
root.Print_tree()
root.in_order()
print()
