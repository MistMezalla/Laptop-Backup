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
                self.left =Tree_node(data,self)

        else:
            if self.right:
                self.right.add_node(data)
            else:
                self.right =Tree_node(data,self)

    def Build_BT_list(self,arr):
        for i in range(len(arr)):
            self.add_node(arr[i])

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

    def min_BT(self):
        min_node = self

        if self.left:
            left_min = self.left.min_BT()
            if left_min.data <= min_node.data:
                min_node = left_min

        if self.right:
            right_min = self.right.min_BT()
            if right_min.data <= min_node.data:
                min_node = right_min

        return min_node

    def max_BT(self):
        max_node = self

        if self.left:
            left_max = self.left.max_BT()
            if left_max.data >= max_node.data:
                max_node = left_max

        if self.right:
            right_max = self.right.max_BT()
            if right_max.data >= max_node.data:
                max_node = right_max

        return max_node

    def __iter__(self):
        if self.left:
            yield from self.left
        yield self.data
        if self.right:
            yield from self.right

    def search(self,data):
        if self.data == data:
            return self

        if self.left:
            left_node = self.left.search(data)
            if left_node:
                return left_node

        if self.right:
            right_node = self.right.search(data)
            if right_node:
                return right_node

        return None

    def depth_node(self,data):
        ptr = self.search(data).parent
        lvl = 0

        while ptr:
            lvl+=1
            ptr = ptr.parent

        return lvl

    def height_node(self):
        if not self:
            return -1

        left_hgt = right_hgt = 0
        if self.left:
            left_hgt = self.left.height_node()

        if self.right:
            right_hgt = self.right.height_node()

        if not self.left and not self.right:
            return 0

        return max(left_hgt,right_hgt) + 1

    def mirror_tree(self):
        if self.left:
            self.left.mirror_tree()
        if self.right:
            self.right.mirror_tree()
        if self.left or self.right:
            self.left,self.right = self.right,self.left

        return self

    '''
    -> This function returns root and not a new_node
    '''
    def clone_tree_as_ref(self):
        if not self.left and not self.right:
            return Tree_node(self.data)

        left_node = right_node = None
        if self.left:
            left_node = self.left.clone_tree()

        if self.right:
            right_node = self.right.clone_tree()

        self.left = left_node
        self.right = right_node

        return self

    def clone_tree(self):
        new_node = Tree_node(self.data)

        if self.left:
            new_node.left = self.left.clone_tree()
            new_node.left.parent = new_node

        if self.right:
            new_node.right = self.right.clone_tree()
            new_node.right.parent = new_node

        return new_node



    def compare_trees(root1,root2):
        if not root1 and not root2:
            return True

        if not (root1 and root2):
            return False

        if root1.data != root2.data:
            return False

        if root1.left and root2.left:
            left_node = root1.left.compare_trees(root2.left)

            if not left_node:
                return False

        else:
            if root1.left or root2.left:
                return False

        if root1.right and root2.right:
            right_node = root1.right.compare_trees(root2.right)

            if not right_node:
                return False

        else:
            if root1.right or root2.right:
                return False

        return True

    def del_BT(self):
        if not self.left and not self.right:
            self.parent = None
            return None

        if self.left:
            left_node = self.left.del_BT()
            self.left = left_node

        if self.right:
            right_node = self.right.del_BT()
            self.right = right_node

    def num_leaf_nodes(self):
        if not self.left and not self.right:
            return 1

        left_leaves = right_leaves = 0
        if self.left:
            left_leaves = self.left.num_leaf_nodes()

        if self.right:
            right_leaves = self.right.num_leaf_nodes()

        return left_leaves + right_leaves

    def num_nodes(self):
        left_nodes = right_nodes = 0
        if self.left:
           left_nodes = self.left.num_nodes()

        if self.right:
            right_nodes = self.right.num_nodes()

        return left_nodes + right_nodes + 1

    def num_int_nodes_alt(self):
        return self.num_nodes() - self.num_leaf_nodes()

    def num_int_nodes(self):
        l_nodes = r_nodes =0
        if self.left:
            l_nodes = self.left.num_int_nodes()

        if self.right:
            r_nodes = self.right.num_int_nodes()

        if self.left or self.right:
            return l_nodes + r_nodes + 1
        else:
            return 0

    def leaf_nodes_in_order(self):
        if self.left:
            self.left.leaf_nodes_in_order()

        if not self.left and not self.right:
            print(self.data,end=" ")

        if self.right:
            self.right.leaf_nodes_in_order()

    def int_nodes_in_order(self):
        if self.left:
            self.left.int_nodes_in_order()

        if self.left or self.right:
            print(self.data, end=" ")

        if self.right:
            self.right.int_nodes_in_order()

    def in_order_pre(self,data):
        node = self.search(data)
        if node.left:
            return node.left.max_BT()
        else:
            return None

    def in_order_succ(self,data):
        node = self.search(data)
        if node.right:
            return node.right.min_BT()
        else:
            return None




root = Tree_node(10)
l = [14,24,19,0,15,2,7,16]
root.Build_BT_list(l)
root.Print_tree()
print(any(x==0 for x in root))
print(f"Found {root.search(110).data if root.search(110) else None}")
print(root.depth_node(0))
print(root.height_node())
root.mirror_tree().Print_tree()
clone = root.clone_tree()
clone.Print_tree()
print(root.compare_trees(clone))
clone.del_BT()
clone.Print_tree()
root.Print_tree()
root.in_order()
print()

print(root.in_order_pre(0).data if root.in_order_pre(0) else None)
print(root.in_order_succ(0).data if root.in_order_succ(0) else None)
print(root.num_leaf_nodes())
print(root.num_nodes())
print(root.num_int_nodes())
print(root.num_int_nodes_alt())
root.int_nodes_in_order()
print()
root.leaf_nodes_in_order()
print()
