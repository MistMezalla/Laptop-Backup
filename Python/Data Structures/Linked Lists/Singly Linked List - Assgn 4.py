class Node:
    def __init__(self, data=None,next=None):
        self.data = data
        self.nxt = next

class Singly_linked_list:
    def __init__(self):
        self.head = None

    def ins_at_st(self, data):
        new_node = Node(data,self.head)
        self.head = new_node

    def print(self):
        ptr = self.head

        if not ptr:
            print("Empty List")
            return

        while ptr:
            print(ptr.data, end="-->")
            ptr = ptr.nxt
        print()

    def length(self):
        ptr = self.head

        cnt = 0
        while ptr:
            cnt+=1
            ptr=ptr.nxt

        return cnt

    def ins_at_end(self, data):
        new_node = Node(data)

        if self.length() == 0:
            self.ins_at_st(data)
            return

        ptr = self.head

        while ptr.nxt:
            ptr=ptr.nxt

        ptr.nxt=new_node

    def ins_bef_val(self,data,val):
        ptr = self.head

        if (ptr.data==val):
            self.ins_at_st(data)
            return
        try:
            while(ptr.nxt.data!=val):
                ptr=ptr.nxt

            new_node = Node(data,ptr.nxt)
            ptr.nxt = new_node
        except Exception as e:
            print(type(e).__name__,": Val entered not in Linked List")

    def ins_aft_val(self,data,val):
        ptr=self.head

        try:
            while ptr.data!=val:
                ptr=ptr.nxt

            new_node=Node(data,ptr.nxt)
            ptr.nxt=new_node
        except Exception as e:
            print(type(e).__name__,": Val entered not in Linked List")

    def ins_at_pos(self,pos,data):
        ptr = self.head

        if pos>=self.length():
            print("Out of bound error")
            return

        cnt=0
        while ptr and cnt!=pos-1:
            ptr=ptr.nxt
            cnt+=1

        new_node=Node(data,ptr.nxt)
        ptr.nxt=new_node

    def del_st(self):
        try:
            self.head = self.head.nxt
        except Exception as e:
            print(type(e).__name__,": Del from Empty List")

    def del_end(self):
        ptr = self.head

        if not ptr.nxt:
            self.del_st()

        while ptr.nxt.nxt:
            ptr=ptr.nxt

        ptr.nxt=None

    def del_bef_val(self, val):
        ptr = self.head

        if (ptr.data==val):
            print("No such data exists bef val entered")
            return

        if ptr.nxt.data==val:
            self.del_st()
            return

        try:
            while(ptr.nxt.nxt.data!=val):
                ptr=ptr.nxt

            ptr.nxt = ptr.nxt.nxt
        except Exception as e:
            print(type(e).__name__,": Val entered not in Linked List")

    def del_aft_val(self, val):
        ptr = self.head


        try:
            while (ptr.data != val):
                ptr = ptr.nxt

            if not (ptr.nxt):
                print("No such data exists aft val entered")
                return

            ptr.nxt = ptr.nxt.nxt
        except Exception as e:
            print(type(e).__name__, ": Val entered not in Linked List")

    def del_at_pos(self,pos):
        ptr = self.head

        if pos>=self.length():
            print("Out of bound error")

        cnt=0
        while ptr and cnt!=pos-1:
            ptr=ptr.nxt
            cnt+=1

        ptr.nxt=ptr.nxt.nxt

    def rev_list(self):
        c = self.head
        p = c
        n = c.nxt

        while n:
            p=c
            c=n
            n=c.nxt
            c.nxt=p

        self.head.nxt=None
        self.head=c

    def rev_list_2_ptr(self):
        curr,prev = self.head,None

        while curr:
            curr.nxt,prev,curr = prev,curr,curr.nxt

        self.head = prev


    def extend_values(self, seq):
        for i in range(len(seq)):
            self.ins_at_end(seq[i])

    def sort_list(self):
        l = []
        ptr = self.head
        for i in range(self.length()):
            l.append(ptr.data)
            self.del_st()
            ptr=self.head

        l.sort()
        self.extend_values(l)

'''
l1 = Singly_linked_list()
l1.ins_at_st(10)
l1.ins_at_st(7)
l1.print()
print(l1.length())

l1.ins_at_end(0)
l1.print()
l1.ins_at_end(-1)
l1.print()
print(l1.length())

l1.ins_bef_val(5,7)
l1.print()
print(l1.length())

l1.ins_aft_val(13,-10)
l1.print()
print(l1.length())

l1.del_st()
l1.print()
print(l1.length())

l1.del_end()
l1.print()
print(l1.length())

l1.ins_at_st(25)
l1.ins_at_end(44)
l1.del_bef_val(0)
l1.print()
l1.del_bef_val(25)
l1.print()
l1.del_bef_val(7)
l1.print()

l1.ins_at_pos(2,50)
l1.ins_at_pos(3,73)
l1.ins_at_pos(1,25)
l1.print()

l1.del_at_pos(1)
l1.print()

l1.rev_list()
l1.print()

l1.sort_list()
l1.print()

l1.extend_values("Hello to one and all".split())
l1.print()

l1.sort_list()
l1.print()
'''
l2 = Singly_linked_list()
l2.extend_values([3,4,2,1])
l2.rev_list_2_ptr()
l2.print()
'''
l2 = Singly_linked_list()
l2.ins_at_st(50)
l2.print()
l2.del_st()
l2.print()
l2.del_st()
l2.print()
l2.ins_at_st(100)
l2.print()
'''


