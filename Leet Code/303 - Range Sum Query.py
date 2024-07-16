class NumArray:

    def __init__(self, nums: list[int]):
        self.arr = []
        self.arr.append(nums[0])


        for i in range(1,len(nums)):
            self.arr.append(nums[i]+self.arr[i-1])


    def sumRange(self, left: int, right: int) -> int:
        if right > 0 and left > 0:
            return self.arr[right] - self.arr[left-1]
        else:
            return self.arr[left or right]



# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)