class Solution:
    def subarraysDivByK(self, nums: list[int], k: int) -> int:
        hash_rem_freq = {0:0}

        pf_sum = 0
        for num in nums:
            pf_sum += num

            if pf_sum % k in hash_rem_freq:
                hash_rem_freq[pf_sum%k] += 1

            else:
                hash_rem_freq[pf_sum%k] = 0

        valid_subarr = 0
        for key,val in hash_rem_freq.items():
            valid_subarr += val*(val+1)//2

        return valid_subarr

