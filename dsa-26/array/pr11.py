class Solution:
    def twoSum(self, nums, target):
        two_sum =[]
        n = len(nums)

        for i in range(0,n-1):
            for j in range(i+1,n):
                if nums[i]+nums[j]==target:
                    two_sum=[i,j]
        return two_sum
        
        