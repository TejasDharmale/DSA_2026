class Solution:
    def moveZeroes(self, nums):
        n = len(nums)
        j = 0
        for i in range(0, n):
            if nums[i] != 0:
                nums[j] = nums[i]
                j += 1
        for k in range(j, n):
            nums[k] = 0

        return nums
