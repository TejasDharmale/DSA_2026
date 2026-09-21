# Boyer-Moore Majority Vote Algorithm


class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        n = len(nums)
        count = 0
        majority = nums[0]

        for i in range(0, n):
            if count == 0:
                count += 1
                majority = nums[i]
            elif majority == nums[i]:
                count += 1
            else:
                count -= 1
        print(majority)
