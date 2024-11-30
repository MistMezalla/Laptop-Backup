from collections import deque

class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        st = deque()


        for ch in expression:
            if ch == ')':
                values = []

                while st[-1] != '(':
                    values.append(st.pop())
                st.pop()
                op = st.pop()

                st.append(self.eval_operation(op,values))

            elif ch != ',':
                st.append(ch)


        return False if st[-1] == 'f' else True

    def eval_operation(self,op,values):
        if op == '!':
            return 't' if values[0] == 'f' else 'f'

        elif op == '&':
            for val in values:
                if val == 'f':
                    return val
            return 't'

        else:
            for val in values:
                if val == 't':
                    return val

            return 'f'



