class Solution:
    def sortZeroOneTwo(self, nums):
        start = 0
        middle = 0
        end = len(nums) - 1

        while middle <= end:
            if nums[middle] == 0:
                nums[start], nums[middle] = nums[middle], nums[start]
                start += 1
                middle += 1

            elif nums[middle] == 1:
                middle += 1

            else:
                nums[middle], nums[end] = nums[end], nums[middle]
                end -= 1

# overwriting apporach


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        count_of_zero = 0
        count_of_one = 0
        count_of_two = 0

        for i in nums:
            if i == 0:
                count_of_zero += 1
            elif i == 1:
                count_of_one += 1
            else:
                count_of_two += 1

# started overwriting in array

        for j in range(0, count_of_zero):
            nums[j] = 0
            j += 1
        for j in range(count_of_zero, count_of_zero+count_of_one):
            nums[j] = 1
            j += 1
        for j in range(count_of_zero+count_of_one, len(nums)):
            nums[j] = 2
            j += 1

        return nums
