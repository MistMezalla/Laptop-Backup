class ListNode:
    def __init__(self, val, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

class TextEditor:
    def __init__(self):
        self.head = self.tail = self.cursor = None
        self.len = 0

    def addText(self, text: str) -> None:
        for letter in text:
            node = ListNode(letter)

            if self.head == self.tail == None:
                self.head = self.tail = self.cursor = node
            elif self.cursor == self.tail:
                node.prev = self.tail
                self.tail.next = node
                self.tail = node
                self.cursor = node
            elif not self.cursor:
                node.next = self.head
                self.head.prev = node
                self.head = node
                self.cursor = self.head
            else:  # Insertion in the middle
                node.prev = self.cursor
                node.next = self.cursor.next
                if self.cursor.next:
                    self.cursor.next.prev = node
                else:
                    self.tail = node
                self.cursor.next = node
                self.cursor = node
            self.len += 1

    def deleteText(self, k: int) -> int:
        cnt_del = 0
        while self.cursor and k > 0:
            cnt_del += 1
            k -= 1
            self.len -= 1

            prev_node = self.cursor.prev
            next_node = self.cursor.next

            if prev_node:
                prev_node.next = next_node
            else:
                self.head = next_node

            if next_node:
                next_node.prev = prev_node
            else:
                self.tail = prev_node

            self.cursor = prev_node

        return cnt_del

    def cursorLeft(self, k: int) -> str:
        while self.cursor and k > 0:
            self.cursor = self.cursor.prev
            k -= 1

        # Collect up to 10 characters to the left of the cursor
        res_str = ""
        node = self.cursor
        for _ in range(10):
            if not node:
                break
            res_str = node.val + res_str
            node = node.prev

        return res_str

    def cursorRight(self, k: int) -> str:
        if not self.cursor:
            self.cursor = self.head
            k -= 1

        while self.cursor and k > 0:
            if self.cursor.next:
                self.cursor = self.cursor.next
            k -= 1

        # Collect up to 10 characters to the left of the cursor
        res_str = ""
        node = self.cursor
        for _ in range(10):
            if not node:
                break
            res_str = node.val + res_str
            node = node.prev



        return res_str

# Testing
editor = TextEditor()

editor.addText("bxyackuncqzcqo")
print(editor.cursorLeft(12))
print(editor.deleteText(3))
print(editor.cursorLeft(5))# Expected output: 4
editor.addText("osdhyvqxf")
print(editor.cursorRight(10)) # Expected output: "etpractice"
# print(editor.cursorLeft(8))  # Expected output: "leet"
# print(editor.deleteText(10))  # Expected output: 4 (only deletes 'leet')
# print(editor.cursorLeft(2))  # Expected output: ""
# print(editor.cursorRight(6))  # Expected output: "practi"
