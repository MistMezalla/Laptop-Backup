class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        i = 0
        j = len(numbers) - 1

        while i <= j:
            temp_sum = numbers[i] + numbers[j]

            if temp_sum == target:
                return [i+1,j+1]

            elif temp_sum > target:
                j-= 1

            else:
                i+=1



sol = Solution()
print(sol.twoSum(numbers = [2,7,11,15], target = 9))
      