class Node:
    def __init__(self,data=None,next=None,prev=None):
        self.data=data
        self.next = next if next is not None else self
        self.prev = prev if prev is not None else self

class Circular_Doubly_Linked_List:
    def __init__(self):
        self.head = None

    def ins_at_st(self,data):
        if not (self.head):
            new_node=Node(data)
            self.head=new_node
            return

        new_node=Node(data,self.head,self.head.prev)
        self.head.prev.next=new_node
        self.head.prev=new_node
        self.head=new_node

    def print_for(self):
        ptr = self.head

        print("Forward:-")
        print(self.head.prev.data,end=" ")
        while ptr.next != self.head:
            print("<--",ptr.data,"-->",end="")
            ptr=ptr.next
        print("<--",self.head.prev.data,"-->")

    def print_rev(self):
        ptr = self.head.prev

        print("Reverse:-")
        print(self.head.data, end=" ")
        while ptr.prev != self.head.prev:
            print("<--", ptr.data, "-->", end="")
            ptr = ptr.prev
        print("<--", self.head.data, "-->")

    def ins_at_end(self,data):
        if not self.head:
            self.ins_at_st(data)
            return

        new_node=Node(data,self.head,self.head.prev)
        self.head.prev.next=new_node
        self.head.prev = new_node

    def length(self):
        ptr = self.head

        if not self.head:
            return 0

        cnt = 1
        while ptr.next != self.head:
            cnt +=1
            ptr=ptr.next

        return cnt

    def ins_at_pos(self,data,pos):
        if pos>=self.length():
            return "Index out of bound"

        if pos==0:
            self.ins_at_st(data)
            return

        ptr = self.head
        cnt = 0
        while cnt!=pos-1:
            cnt+=1
            ptr=ptr.next

        new_node=Node(data,ptr.next,ptr)
        ptr.next.prev=new_node
        ptr.next=new_node

    def ins_bef_val(self,data,val):
        ptr = self.head

        try:
            while ptr.next.data != val:
                ptr = ptr.next

            new_node = Node(data, ptr.next, ptr)
            ptr.next.prev = new_node
            ptr.next = new_node
        except Exception as e:
            print(type(e).__name__,"Val entered not found")

    def ins_aft_val(self, data, val):
        ptr = self.head

        try:
            while ptr.data != val:
                ptr = ptr.next

            new_node = Node(data, ptr.next, ptr)
            ptr.next.prev = new_node
            ptr.next = new_node
        except Exception as e:
            print(type(e).__name__, "Val entered not found")

    def del_st(self):
        if not self.head:
            return "Empty List"

        if self.head.next == self.head:
            self.head=None
            return

        self.head.next.prev=self.head.prev
        self.head.prev.next=self.head.next
        self.head=self.head.next

    def del_end(self):
        if not self.head:
            return "Empty List"

        if self.head.next == self.head:
            self.head=None
            return

        self.head.prev.prev.next = self.head
        self.head.prev = self.head.prev.prev

    def rev_list(self):
        ptr = self.head

        while ptr.next != self.head:
            ptr.next,ptr.prev=ptr.prev,ptr.next
            ptr=ptr.prev

        ptr.next, ptr.prev = ptr.prev, ptr.next

        self.head = self.head.next





l1 = Circular_Doubly_Linked_List()
l1.ins_at_st(10)
l1.print_for()
l1.ins_at_st(15)
l1.print_for()
l1.ins_at_st(0)
l1.ins_at_st(20)
l1.print_for()
l1.print_rev()

l1.ins_at_end(50)
l1.print_for()
l1.print_rev()
l1.ins_at_end(27)
l1.print_for()
l1.print_rev()

l1.ins_at_pos(100,2)
l1.ins_bef_val(80,15)
l1.ins_aft_val(-25,27)
l1.print_for()
l1.print_rev()

l1.del_st()
l1.print_for()
l1.print_rev()

l1.del_end()
l1.print_for()
l1.print_rev()

print("Rev list Tests:-")
l1.print_for()
l1.print_rev()
l1.rev_list()
l1.print_for()
l1.print_rev()