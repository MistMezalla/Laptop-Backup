'''
-> This solution is very slow as O(n) but can be achieved in O(1) as well
'''
from collections import deque
class BrowserHistory:

    def __init__(self, homepage: str):
        self.pri_st = deque()
        self.sec_st = deque()
        self.pri_st.append(homepage)

    def visit(self, url: str) -> None:
        self.sec_st.clear()
        self.pri_st.append(url)


    def back(self, steps: int) -> str:
        x = 0
        while len(self.pri_st) > 1 and x<steps:
            x+=1
            self.sec_st.append(self.pri_st.pop())

        return self.pri_st[-1]

    def forward(self, steps: int) -> str:
        x = 0
        while len(self.sec_st) != 0 and x < steps:
            x += 1
            self.pri_st.append(self.sec_st.pop())

        return self.pri_st[-1]


def test_browser_history():
    browser_history = BrowserHistory("leetcode.com")

    # Visit some URLs
    browser_history.visit("google.com")

    print(browser_history.back(7))
    print(browser_history.back(7))
    print(browser_history.forward(5))
    print(browser_history.forward(1))

    browser_history.visit("facebook.com")
    browser_history.visit("youtube.com")

    print(browser_history.back(9))


test_browser_history()

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)