class Tree_node():
    def __init__(self,data,parent = None):
        self.data = data
        self.left = None
        self.right = None
        self.parent = parent

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


def Build_BT_pre_in(pre_order,in_order,parent = None):
    root = Tree_node(pre_order[0],parent)

    in_order_left = in_order[:in_order.index(pre_order[0])]
    in_order_right = in_order[in_order.index(pre_order[0])+1:]
    pre_order_left = pre_order[1:len(pre_order) - len(in_order_right)]
    pre_order_right = pre_order[len(pre_order)-len(in_order_right):]

    left_node = right_node = None
    if in_order_left:
        left_node = Build_BT_pre_in(pre_order_left,in_order_left,root)
        root.left = left_node

    if in_order_right:
        right_node = Build_BT_pre_in(pre_order_right,in_order_right,root)
        root.right = right_node

    return root

def Build_BT_Post_in(post_order,in_order,parent = None):
    root = Tree_node(post_order[-1],parent)

    in_order_left = in_order[:in_order.index(post_order[-1])]
    in_order_right = in_order[in_order.index(post_order[-1])+1:]
    post_order_left = post_order[:len(in_order_left)]
    post_order_right = post_order[len(in_order_left):len(post_order)-1]

    if in_order_left:
        left_node = Build_BT_Post_in(post_order_left,in_order_left,root)
        root.left = left_node

    if in_order_right:
        right_node = Build_BT_Post_in(post_order_right,in_order_right,root)
        root.right = right_node

    return root

pre_order = [3,9,20,15,7]
in_order = [9,3,15,20,7]
post_order = [9,15,7,20,3]

BT_1 = Build_BT_pre_in(pre_order,in_order)
BT_1.Print_tree()
BT_1.in_order()
print()

BT_2 = Build_BT_Post_in(post_order,in_order)
BT_2.Print_tree()
BT_2.in_order()
print()





