class Solution:
    def interpret(self, command: str) -> str:
        buf = ''
        ret_str = ''
        d = dict(zip(('G', '()', '(al)'), ('G', 'o', 'al')))
        for i in range(len(command)):
            buf += command[i]
            if buf in d:
                ret_str += d[buf]
                buf = ''

        return ret_str


