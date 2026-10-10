class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        n = len(nums)
        res = 0

        for i in range(0, n):
            res = target - nums[i]
            if res in nums:
                x = nums.index(res)

                if x != i:
                    return [x, i]

# but best approach is to use hashmap
        seen = {}
        for i, n in enumerate(nums):
            if target - n in seen:
                return [seen[target - n], i]
            seen[n] = i
