class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        l = sentence.split()
        vow = "aeiou"

        for i in range(len(l)):
            if l[i][0].lower() in vow:
                l[i]+="ma"
            else:
                temp = list(l[i])
                st = temp.pop(0)
                temp.append(st)
                l[i] = "".join(temp)
                l[i]+='ma'

            l[i]+=(i+1)*"a"

        return " ".join(l)
