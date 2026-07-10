class Solution:
    def missingNumber(self, nums):
        n = len(nums)

        for i in range(0,n):
            sums = n*(n+1)//2
            a =sum(nums)
            missing = sums -a
        return missing
        