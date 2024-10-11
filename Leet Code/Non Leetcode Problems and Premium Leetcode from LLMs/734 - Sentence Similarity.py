class Solution:
    def Sim_Sentence(self,sentence1 : list[str],sentence2 : list[str],simPairs : list[list[str]]) -> bool:
        if len(sentence1) != len(sentence2):
            return False

        hash_pairs = {key: val for key,val in simPairs}

        for i in range(len(sentence2)):
            if sentence1[i] == sentence2[i]:
                continue

            elif sentence1[i] not in hash_pairs or hash_pairs[sentence1[i]] != sentence2[i]:
                return False


        return True

sol = Solution()
#Test Case 1 => Passed
print(sol.Sim_Sentence(sentence1 = ["I", "enjoy", "coding"],
sentence2 = ["I", "like", "programmin"],
simPairs = [["enjoy", "like"], ["coding", "programming"]]))
# Test case 2 => Passed
print(sol.Sim_Sentence(sentence1 = ["I", "enjoy", "running"],
sentence2 = ["I", "like", "jogging"],
simPairs = [["enjoy", "like"], ["running", "jogging"], ["happy", "joyful"]]))
# Test Case 3 => Passed
print(sol.Sim_Sentence(sentence1 = ["I", "love", "coding"],
sentence2 = ["I", "love", "coding"],
simPairs = [["love", "enjoy"], ["coding", "programming"]]
))
# Test Case 4 => Passed
print(sol.Sim_Sentence(sentence1 = ["I", "am", "happy"],
sentence2 = ["I", "am", "joyful"],
simPairs = [["happy", "joyful"], ["sad", "unhappy"]]
))
# Test Case 5 => Passed
print(sol.Sim_Sentence(sentence1 = ["I", "am", "happy"],
sentence2 = ["You", "are", "sad"],
simPairs = [["happy", "joyful"]],
))
# Test Case 6 => Passed
print(sol.Sim_Sentence(sentence1 = ["The", "bank", "will", "reopen"],
sentence2 = ["The", "bank", "is", "closed"],
simPairs = [["bank", "bank"], ["reopen", "closed"]]
))
# Test Case 7 => Passed
print(sol.Sim_Sentence(sentence1 = ["The", "cat", "is", "cute"],
sentence2 = ["The", "dog", "was", "adorable"],
simPairs = [["cute", "adorable"]]
))
# Test Case 8 => Passed          ----
--print(sol.Sim_Sentence(sentence1 = ["I", "am", "working"],
sentence2 = ["They", "are", "playing"],
simPairs = []
))

