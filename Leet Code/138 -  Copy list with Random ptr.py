from typing import Optional
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None

        hsh = dict()

        node = head
        hsh[None] = None
        while node:
            hsh[node] = Node(node.val)
            node = node.next

        node = head
        while node:
            cpy = hsh[node]
            cpy.next = hsh[node.next]
            cpy.random = hsh[node.random]
            node = node.next

        return hsh[head]


def create_linked_list_with_random_pointers(values, random_indices):
    if not values:
        return None

    nodes = [Node(x) for x in values]
    for i, node in enumerate(nodes):
        if i < len(nodes) - 1:
            node.next = nodes[i + 1]
        if random_indices[i] is not None:
            node.random = nodes[random_indices[i]]
    return nodes[0]


def print_linked_list_with_random_pointers(head):
    node = head
    while node:
        random_val = node.random.val if node.random else None
        print(f'Node value: {node.val}, Random points to: {random_val}')
        node = node.next


def verify_deep_copy(original, copied):
    original_nodes = []
    copied_nodes = []

    o = original
    c = copied
    while o and c:
        original_nodes.append(o)
        copied_nodes.append(c)
        o = o.next
        c = c.next

    if o or c:
        return False

    for o_node, c_node in zip(original_nodes, copied_nodes):
        if o_node is c_node:
            return False
        if o_node.val != c_node.val:
            return False
        if (o_node.random and c_node.random and o_node.random.val != c_node.random.val) or \
                (o_node.random is None and c_node.random is not None) or \
                (o_node.random is not None and c_node.random is None):
            return False
    return True


# Test example
values = [7, 13, 11, 10, 1]
random_indices = [None, 0, 4, 2, 0]

head = create_linked_list_with_random_pointers(values, random_indices)
solution = Solution()
copied_head = solution.copyRandomList(head)

print("Original list:")
print_linked_list_with_random_pointers(head)
print("\nCopied list:")
print_linked_list_with_random_pointers(copied_head)

print("\nVerification of deep copy:")
print(verify_deep_copy(head, copied_head))

