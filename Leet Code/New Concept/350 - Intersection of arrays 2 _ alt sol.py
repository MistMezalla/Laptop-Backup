'''
-> Here all the followups sol are given
'''

#Followup 1:-
'''
-> If both the arrays are sorted already
    -> then just follow my sol(2 ptr approach)
'''

#Followup 2:-
'''
-> If len(array1) << len(array2)
    -> hash the freq of occurrence of each elem on array1 and cmp the elem elem of array2 with the hash values.
'''
class Solution2:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        freq ={}

        for num in nums1:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        res = []
        for num in nums2:
            if num in freq and freq[num] > 0:
                res.append(num)
                freq[num] -= 1

        return res

# Followup 3:-
'''
-> If array2 is stored on the disk and processed in chunks
    -> Same hashing method as Followup2
    -> Only improvement lies in the ranges of for loops to take in into acc chunk processing
'''
class Solution3:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        ram_size = 10
        max_size = 1001


        res = []
        for i in range(0,max_size,ram_size):
            freq = {}
            for num in nums1:
                if i<= num <i+ram_size:
                    if num in freq:
                        freq[num] += 1
                    else:
                        freq[num] = 1

            for num in nums2:
                if i <= num < i+ram_size and num in freq and freq[num] > 0:
                    res.append(num)
                    freq[num] -= 1

        return res

