class Solution(object):
    def interpret(self, command):
        buf = ''
        ret_str = ''
        d = dict(zip(('G', '()', '(al)'), ('G', 'o', 'al')))
        for i in range(len(command)):
            buf += command[i]
            if buf in d:
                ret_str += d[buf]
                buf = ''

        return ret_str

# For local testing
if __name__ == "__main__":
    sol = Solution()
    command = input("Enter the input string: ")
    print(sol.interpret(command))
