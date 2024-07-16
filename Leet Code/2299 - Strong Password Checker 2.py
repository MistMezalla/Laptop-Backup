class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        sp_char = "!@#$%^&*()-+"

        if len(password) < 8:
            return False

        low = upper = dig = sp =0
        for i in range(len(password)):
            if i>0 and password[i] == password[i-1]:
                return False
            if password[i].islower():
                low+=1
            elif password[i].isupper():
                upper+=1
            elif password[i].isdigit():
                dig+=1
            elif password[i] in sp_char:
                sp += 1


        if low*upper*dig*sp == 0:
            return False

        return True

sol = Solution()
print(sol.strongPasswordCheckerII("IloveLe3tcode!"))