class Solution:
    def rotateArrayByOne(self, nums):
        n= len(nums)
        j= nums[0]

        for i in range(1,n):
            nums[i-1]=nums[i]
        nums[-1]=j 
        return nums   