class Solution:
    def leaders(self, nums):
        n = len(nums)
        res = []
        for i in range(0, n):
            for j in range(i+1, n):
                if nums[i] < nums[j]:
                    break

            else:
                res.append(nums[i])

        return res
