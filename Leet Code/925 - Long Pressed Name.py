class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        ptr = 0
        typed = list(typed)
        for i in range(len(name)):
            if ptr>=len(typed):
                return False
            if name[i] == typed[ptr]:
                if i+1<len(name) and name[i] == name[i+1]:
                    ptr+=1
                else:
                    typed.pop(ptr+1)
                    ptr+=1
            else:
                return False

        if typed:
            return True
        return False

sol =  Solution()
print(sol.isLongPressedName("alex","aaleex"))
