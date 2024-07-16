class ListNode:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

class FrontMiddleBackQueue:
    def __init__(self):
        self.len = 0
        self.head = None
        self.tail = None
        self.middle = None

    def pushFront(self, val: int) -> None:
        if self.head is None:
            self.head = self.middle = self.tail = ListNode(val)

        else:
            new_node = ListNode(val)
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

        self.len += 1

        if not self.len & 1: #even
            self.middle = self.middle.prev

    def pushMiddle(self, val: int) -> None:
        if self.middle is None:
            self.head = self.middle = self.tail = ListNode(val)
            self.len += 1

        elif self.len == 1 or self.len == 2:
            self.pushFront(val)

        else:
            new_node = ListNode(val,self.middle,self.middle.prev)
            self.middle.prev.next = new_node
            self.middle.prev = new_node
            self.len += 1


        if not self.len & 1:
            self.middle = self.middle.prev

    def pushBack(self, val: int) -> None:
        if self.tail is None:
            self.head = self.middle = self.tail = ListNode(val)

        else:
            new_node = ListNode(val)
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

        self.len += 1


        if self.len > 1 and self.len & 1:
            self.middle = self.middle.next


    def popFront(self) -> int:
        if self.head is None:
            return -1

        data = self.head.val
        self.head = self.head.next
        if self.head:
            self.head.prev = None

        self.len -= 1
        if self.len & 1:
            self.middle = self.middle.next

        return data

    def popMiddle(self) -> int:
        Prev = Next = data = None
        if self.tail is None:
            return -1
        elif self.len == 1 or self.len == 2:
            self.popFront()
        else:
            Prev = self.middle.prev
            Next = self.middle.next
            data = self.middle.val
            self.middle.prev.next = self.middle.next
            self.middle.next.prev = Prev
            self.len -= 1


        if self.len & 1:
            self.middle = Next
        else:
            self.middle = Prev

        return data

    def popBack(self) -> int:
        if self.tail is None:
            return -1

        data = self.tail.val
        self.tail = self.tail.prev
        if self.tail:
            self.tail.next = None

        self.len -= 1
        if not self.len & 1:
            self.middle = self.middle.prev

        return data

def test_pushFront():
    q = FrontMiddleBackQueue()
    q.pushFront(1)
    q.pushFront(2)
    q.pushFront(3)
    print("After pushFront operations: 3 -> 2 -> 1")
    print_linked_list(q.head)  # Expected: 3 -> 2 -> 1

def test_pushMiddle():
    q = FrontMiddleBackQueue()
    q.pushFront(1)
    q.pushFront(2)
    q.pushMiddle(3)
    print("After pushMiddle operation: 2 -> 3 -> 1")
    print_linked_list(q.head)  # Expected: 2 -> 3 -> 1

def test_pushBack():
    q = FrontMiddleBackQueue()
    q.pushBack(1)
    q.pushBack(2)
    q.pushBack(3)
    print("After pushBack operations: 1 -> 2 -> 3")
    print_linked_list(q.head)  # Expected: 1 -> 2 -> 3

def test_popFront():
    q = FrontMiddleBackQueue()
    q.pushFront(1)
    # q.pushFront(2)
    # q.pushFront(3)
    print("Before popFront operation: 3 -> 2 -> 1")
    print_linked_list(q.head)  # Expected: 3 -> 2 -> 1
    print("popFront:", q.popFront())  # Expected: 3
    print("After popFront operation:")
    print_linked_list(q.head)  # Expected: 2 -> 1

def test_popMiddle():
    q = FrontMiddleBackQueue()
    q.pushFront(1)
    q.pushFront(2)
    q.pushFront(3)
    q.pushMiddle(4)
    print("Before popMiddle operation: 3 -> 4 -> 2 -> 1")
    print_linked_list(q.head)  # Expected: 3 -> 4 -> 2 -> 1
    print("popMiddle:", q.popMiddle())  # Expected: 4
    print("After popMiddle operation:")
    print_linked_list(q.head)  # Expected: 3 -> 2 -> 1

# def test_popBack():
#     q = FrontMiddleBackQueue()
#     q.pushBack(1)
#     q.pushBack(2)
#     q.pushBack(3)
#     print("Before popBack operation: 1 -> 2 -> 3")
#     print_linked_list(q.head)  # Expected: 1 -> 2 -> 3
#     print("popBack:", q.popBack())  # Expected: 3
#     print("After popBack operation:")
#     print_linked_list(q.head)  # Expected: 1 -> 2

def test_case():
    q = FrontMiddleBackQueue()
    q.pushFront(1)
    print_linked_list(q.head)

    q.pushFront(2)
    print_linked_list(q.head)

    q.pushMiddle(3)
    print_linked_list(q.head)

    q.pushMiddle(4)
    print_linked_list(q.head)

def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=" -> " if current.next else "")
        current = current.next
    print()

# Running the tests
# test_pushFront()
# test_pushMiddle()
# test_pushBack()
# test_popFront()
# test_popMiddle()
#test_popBack()
test_case()

# Your FrontMiddleBackQueue object will be instantiated and called as such:
# obj = FrontMiddleBackQueue()
# obj.pushFront(val)
# obj.pushMiddle(val)
# obj.pushBack(val)
# param_4 = obj.popFront()
# param_5 = obj.popMiddle()
# param_6 = obj.popBack()