'''
-> In this O(1) implementation:-
    -> Used an arr
    -> use index pointers(perfect mathematical formulations) to mimic the stack like behaviour but not use stack data
    str dir(only make use of dynamic arr)
'''

class BrowserHistory:
    def __init__(self,homepage: str):
        self.URLs = [homepage]
        self.curr_url = 0
        self.last_url = 0

    def visit(self,url: str):
        self.curr_url += 1
        if len(self.URLs) > self.curr_url:
            self.URLs[self.curr_url] = url
        else:
            self.URLs.append(url)
        self.last_url = self.curr_url

    def back(self,steps: int)->str:
        self.curr_url = max(0,self.curr_url-steps)
        return self.URLs[self.curr_url]

    def forward(self,steps: int):
        self.curr_url = min(self.last_url, self.curr_url + steps)
        return self.URLs[self.curr_url]


