'''
-> Codeforces blog qns: from video number 62 of the playlist
'''
def codeforces_Qn():
    workers = 3
    masks = [0]*workers
    for i in range(workers):
        working_days =int(input())
        mask = 0
        for j in range(working_days):
            day=int(input())
            mask = mask | 1<<day
        masks[i] = mask

    for i in range(workers):
        for j in range(i+1,workers):
            common = masks[i] & masks[j]
            print(f"common days bet {i+1} and {j+1} = {common.bit_count()}")

def subset_generation_bits():
    def generate(nums: list[int]):
        n = len(nums)
        num_subsets = 1<<n
        power_set = []
        for mask in range(num_subsets):
            subset = []
            for i in range(n):
                if (mask & 1<<i != 0):
                    subset.append(nums[i])
            power_set.append(subset)

        return power_set

    print(generate([1,2,3]))

#codeforces_Qn
subset_generation_bits()

