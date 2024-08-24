'''
-> My sol(doubly linked list based) was not wrong but was lengthy and had too many edge cases to be handled
-> Hence stack based sol overcomes issue of too many edge cases
'''

from collections import deque
class TextEditor:
    def __init__(self):
        self.left = deque()
        self.right = deque()

    def addText(self, text: str) -> None:
        self.left.extend(text)

    def deleteText(self, k: int) -> int:
        cnt = 0
        while self.left and cnt < k:
            cnt+=1
            self.left.pop()

        return cnt

    def cursorLeft(self, k: int) -> str:
        while self.left and k:
            self.right.appendleft(self.left.pop())
            k-=1

        return ''.join(self.get_last_n_char(self.left,10))

    def cursorRight(self, k: int) -> str:
        while self.right and k:
            self.left.append(self.right.popleft())
            k-=1

        return ''.join(self.get_last_n_char(self.left,10))

    def get_last_n_char(self,deq,n: int):
        return [deq[i] for i in range(max(0,len(deq)-n),len(deq))]

# Your TextEditor object will be instantiated and called as such:
# obj = TextEditor()
# obj.addText(text)
# param_2 = obj.deleteText(k)
# param_3 = obj.cursorLeft(k)
# param_4 = obj.cursorRight(k)